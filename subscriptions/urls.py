from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SubscriptionViewSet
from . import views

router = DefaultRouter()
router.register(r'subscriptions', SubscriptionViewSet, basename='subscription')

urlpatterns = [
    path('', include(router.urls)),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
]