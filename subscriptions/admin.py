from django.contrib import admin
from .models import Category, Subscription

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'price', 'currency', 'billing_cycle', 'start_date', 'is_active',)
    list_filter = ('is_active', 'billing_cycle', 'category', 'user',)
    search_fields = ('name', 'user__username',)
    ordering = ('-start_date',)