from django.urls import include, path
from rest_framework import routers

from .utils import generate_and_send_confirmation_code_to_email
from .views import (APISignUp, APIToken, UserViewSet, ReviewViewSet,
                    CommentViewSet, TitleViewSet,
                    CategoryViewSet, GenreViewSet)

router = routers.DefaultRouter()
router.register('users', UserViewSet, basename='User')
router.register('titles', TitleViewSet, basename='Title')
# router.register(r'categories/(?P<slug>\d+)/', CategoryViewSet, basename='Category_object')
router.register('categories', CategoryViewSet, basename='Category')
router.register('genres', GenreViewSet, basename='Genre')
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews')
router.register(
    r'titles/(?P<titles_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)


urlpatterns = [
    path(
        'v1/categories/<slug:slug>/',
        CategoryViewSet.as_view({'delete': 'destroy'}),
        name='del'
    ),
    path(
        'v1/genres/<slug:slug>/',
        GenreViewSet.as_view({'delete': 'destroy'}),
        name='del'
    ),
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
