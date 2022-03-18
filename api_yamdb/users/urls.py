from django.urls import path

from api.views import APIToken, APISignUp


urlpatterns = [
    path(
        'token/',
        APIToken.as_view(),
        name='token'
    ),
    path(
        'signup/',
        APISignUp.as_view(),
        name='signup'
    ),
]
