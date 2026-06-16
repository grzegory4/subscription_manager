from rest_framework import serializers
from .models import Subscription, Category, Profile
from django.contrib.auth.models import User

class SubscriptionSerializer(serializers.ModelSerializer):
    days_until_payment = serializers.ReadOnlyField()
    currency = serializers.CharField(source='price_currency')

    class Meta:
        model = Subscription
        fields = [
            'id', 'name', 'price', 'currency', 'billing_cycle', 
            'start_date', 'category', 'is_active', 'next_billing_date', 
            'days_until_payment'
        ]
        read_only_fields = ['user']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name',)

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('default_currency',)

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
