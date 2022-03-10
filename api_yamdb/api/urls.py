from django.urls import include, path
from rest_framework import routers

from .utils import generate_and_send_confirmation_code_to_email
from .views import (APISignUp, APIToken, UserViewSet, ReviewViewSet,
                    CommentViewSet)

router = routers.DefaultRouter()
router.register('users', UserViewSet, basename='User')
router.register(
    r'titles/reviews',
    ReviewViewSet, basename='reviews')
router.register(
    r'titles/reviews/comments',
    CommentViewSet, basename='comments')


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
