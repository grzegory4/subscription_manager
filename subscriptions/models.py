from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from decimal import Decimal
from django.utils import timezone
import datetime
from datetime import timedelta
from djmoney.models.fields import MoneyField
from djmoney.money import Money
from django.db.models.signals import post_save
from django.dispatch import receiver

class Category(models.Model):
    """categories dictionary"""
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    default_currency = models.CharField(max_length=3, default='PLN')

    def __str__(self):
        return f"Profile of {self.user.username}"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Subscription(models.Model):
    """user main subscription entry"""

    # choices definition
    class BillingCycle(models.TextChoices):
        MONTHLY = "monthly", "Miesięczny"
        YEARLY = "yearly", "Roczny"

    # relations (FK)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="subscriptions")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    # basic data
    name = models.CharField(max_length=100)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='PLN')
    billing_cycle = models.CharField(max_length=10, choices=BillingCycle.choices, default=BillingCycle.MONTHLY)

    # dates and states
    start_date = models.DateField()
    trial_ends_at = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.user.username}"

    def convert_to_currency(self, amount, target_currency='PLN'):
        """Simple currency conversion for stats"""
        if not amount:
            return Decimal('0.00')
            
        source_currency = str(amount.currency)
        target_currency = str(target_currency)
        
        if source_currency == target_currency:
            return amount.amount
        
        # approximate rates relative to PLN
        rates_to_pln = {
            'PLN': Decimal('1.00'),
            'USD': Decimal('4.00'),
            'EUR': Decimal('4.30'),
        }
        
        pln_value = amount.amount * rates_to_pln.get(source_currency, Decimal('1.00'))
        target_value = pln_value / rates_to_pln.get(target_currency, Decimal('1.00'))
        
        return target_value

    def monthly_cost(self):
        if not self.price:
            return Money(0, 'PLN')
        if self.billing_cycle == "monthly":
            return self.price
        return self.price / 12

    def next_billing_date(self):
        today = timezone.now().date()
        
        # if there is a trial and it hasn't ended yet
        if self.trial_ends_at and self.trial_ends_at >= today:
            return self.trial_ends_at
            
        base_date = self.trial_ends_at if self.trial_ends_at else self.start_date
        
        if self.billing_cycle == "monthly":
            return base_date + timedelta(days = 30)
        return base_date + timedelta(days = 365)
    
    @property
    def is_trial(self):
        if not self.trial_ends_at:
            return False
        return self.trial_ends_at >= timezone.now().date()
    
    @property
    # returns number of days till next payment
    def days_until_payment(self):
        next_date = self.next_billing_date()
        if isinstance(next_date, datetime.datetime):
            next_date = next_date.date()

        delta = next_date - timezone.now().date()
        return delta.days
    
    @property
    # returns True if payment will be made in the next 3 days
    def is_urgent(self):
        days = self.days_until_payment
        return 0 <= days <= 3
