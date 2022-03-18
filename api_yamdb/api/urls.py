from django.urls import include, path
from rest_framework import routers

from .views import (UserViewSet, ReviewViewSet,
                    CommentViewSet, TitleViewSet,
                    CategoryViewSet, GenreViewSet)

router_v1 = routers.DefaultRouter()
router_v1.register('users', UserViewSet, basename='user')
router_v1.register('titles', TitleViewSet, basename='title')
router_v1.register('categories', CategoryViewSet, basename='category')
router_v1.register('genres', GenreViewSet, basename='genre')
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews')
router_v1.register(
    r'titles/(?P<titles_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)


urlpatterns = [
    path(
        'v1/categories/<slug:slug>/',
        CategoryViewSet.as_view({'delete': 'destroy'}),
        name='delete_category'
    ),
    path(
        'v1/genres/<slug:slug>/',
        GenreViewSet.as_view({'delete': 'destroy'}),
        name='delete_genre'
    ),
    path('v1/', include(router.urls)),
    path('v1/auth/', include('users.urls')),
]
