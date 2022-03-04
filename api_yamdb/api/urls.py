from django.urls import path, include
from rest_framework import routers
from .views import (
    UserViewSet,
    APISignUp,
    APIToken,
)
from .utils import generate_and_send_confirmation_code_to_email

router = routers.DefaultRouter()
router.register('users', UserViewSet, basename='User')

urlpatterns = [
    path('v1/', include(router.urls)),
    path(
        'v1/auth/email/',
        generate_and_send_confirmation_code_to_email,
        name='confirmation_code'
    ),
    path(
        'v1/auth/token/',
        APIToken.as_view(),
        name='token'
    ),
    path(
        'v1/auth/signup/',
        APISignUp.as_view(),
        name='signup'
    ),
]
