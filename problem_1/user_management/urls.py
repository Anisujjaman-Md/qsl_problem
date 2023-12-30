from django.urls import path, include
from rest_framework import routers
from .views import LoginView, CustomRefreshTokenAPIView
from .views import UserRegistrationViewSet, UserProfileDetailViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('registration', UserRegistrationViewSet, basename='user_registration')
router.register('profile', UserProfileDetailViewSet, basename='user')
router.register('user-list', UserViewSet, basename='user-list')

urlpatterns = [
    path('user/', include(router.urls)),
    path('user/login/', LoginView.as_view(), name='login'),
    path('user/refresh-token/', CustomRefreshTokenAPIView.as_view(), name='refresh_token'),
]
