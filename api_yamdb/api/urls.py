from django.urls import include, path
from rest_framework import routers

from .views import (UserViewSet, ReviewViewSet,
                    CommentViewSet, TitleViewSet,
                    CategoryViewSet, GenreViewSet)

router = routers.DefaultRouter()
router.register('users', UserViewSet, basename='User')
router.register('titles', TitleViewSet, basename='Title')
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
        CategoryViewSet.as_view({'delete': 'delete_category'}),
        name='del'
    ),
    path(
        'v1/genres/<slug:slug>/',
        GenreViewSet.as_view({'delete': 'delete_genre'}),
        name='del'
    ),
    path('v1/', include(router.urls)),
    path('v1/auth/', include('users.urls')),
]
