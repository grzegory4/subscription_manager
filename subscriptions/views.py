from django.shortcuts import render
from rest_framework import viewsets, status
from .models import Subscription, Category, Profile
from .serializers import SubscriptionSerializer, RegisterSerializer, CategorySerializer, ProfileSerializer, ChangePasswordSerializer
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Sum, Max, Count
from decimal import Decimal
import logging

logger = logging.getLogger(__name__)

class SubscriptionViewSet(viewsets.ModelViewSet):
    serializer_class = SubscriptionSerializer

    def get_queryset(self):
        # user x will never see user y subscriptions
        return Subscription.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        # automaticly assign new subscription to logged user
        serializer.save(user=self.request.user)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'billing_cycle']

@login_required
def dashboard(request):
    user_subscriptions = Subscription.objects.filter(user=request.user, is_active=True)
    profile, created = Profile.objects.get_or_create(user=request.user)
    target_currency = profile.default_currency
    
    total_monthly = sum(sub.convert_to_currency(sub.monthly_cost(), target_currency) for sub in user_subscriptions)
    total_count = user_subscriptions.count()
    
    most_expensive = 0
    if user_subscriptions:
        most_expensive = max(sub.convert_to_currency(sub.price, target_currency) for sub in user_subscriptions)

    context = {
        "subscriptions": user_subscriptions,
        "total_monthly": round(float(total_monthly), 2),
        "total_count": total_count,
        "most_expensive": round(float(most_expensive), 2),
        "currency": target_currency,
    }
    return render(request, 'subscriptions/dashboard.html', context)

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]

class SubscriptionStatsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        subscriptions = Subscription.objects.filter(user=user, is_active=True)
        profile, created = Profile.objects.get_or_create(user=user)
        target_currency = profile.default_currency
        
        # debugging
        print(f"DEBUG: Found {subscriptions.count()} active subscriptions for user {user.username}. Target currency: {target_currency}")

        try:
            total_monthly = sum(sub.convert_to_currency(sub.monthly_cost(), target_currency) for sub in subscriptions)
            
            # yearly cost calculation
            total_yearly = 0
            for sub in subscriptions:
                if sub.billing_cycle == 'yearly':
                    total_yearly += sub.convert_to_currency(sub.price, target_currency)
                else:
                    total_yearly += sub.convert_to_currency(sub.price, target_currency) * 12

            # calculate category distribution in target currency
            category_map = {}
            for sub in subscriptions:
                cat_name = sub.category.name if sub.category else "Brak kategorii"
                cost = sub.convert_to_currency(sub.monthly_cost(), target_currency)
                category_map[cat_name] = category_map.get(cat_name, Decimal('0')) + cost

            category_stats = [
                {'category__name': name, 'total': float(total)}
                for name, total in category_map.items()
            ]
            category_stats.sort(key=lambda x: x['total'], reverse=True)

            data = {
                'total_monthly_cost': round(float(total_monthly), 2),
                'total_yearly_cost': round(float(total_yearly), 2),
                'subscriptions_count': subscriptions.count(),
                'category_distribution': category_stats,
                'currency': target_currency
            }
            return Response(data)
        except Exception as e:
            logger.error(f"Error calculating stats: {str(e)}", exc_info=True)
            return Response({'error': str(e)}, status=500)

class ProfileDetailView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer

    def get_object(self):
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile

class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            if user.check_password(serializer.data.get('old_password')):
                user.set_password(serializer.data.get('new_password'))
                user.save()
                return Response({'message': 'Hasło zostało zmienione.'}, status=status.HTTP_200_OK)
            return Response({'error': 'Stare hasło jest niepoprawne.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
