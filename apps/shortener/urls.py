from django.urls import path

from .views import Home, shorten_url_view, redirect_to_login, redirect_url_to_original

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("<str:shortened>/", redirect_url_to_original, name="redirect_to_original"),
    path("/shorten", shorten_url_view, name="shorten_url"),
    path("/redirect-to-login/", redirect_to_login, name="redirect-to-login"),
]
