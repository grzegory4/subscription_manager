from django.shortcuts import render
from rest_framework import viewsets
from .models import Subscription, Category
from .serializers import SubscriptionSerializer, RegisterSerializer
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Sum, Max, Count
from .serializers import CategorySerializer

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
    total_monthly = sum(sub.monthly_cost() for sub in user_subscriptions)
    total_count = user_subscriptions.count()
    most_expensive = user_subscriptions.aggregate(Max('price'))['price__max']

    context = {
        "subscriptions": user_subscriptions,
        "total_monthly": round(total_monthly, 2),
        "total_count": total_count,
        "most_expensive": most_expensive, 
    }
    return render(request, 'subscriptions/dashboard.html', context)

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permisiion_classes = [AllowAny]

class SubscriptionStatsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        subscriptions = Subscription.objects.filter(user=user, is_active=True)

        total_monthly = sum(sub.monthly_cost() for sub in subscriptions)

        category_stats = subscriptions.values('category__name').annotate(
            total=Sum('price')
        ).order_by('-total')

        return Response({
            'total_monthly_cost': round(total_monthly, 2),
            'subscriptions_count': subscriptions.count(),
            'category_distribution': category_stats
        })