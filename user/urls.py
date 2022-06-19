from django.urls import path
from .views import (
    LoginView,
    SignUpView,
    LogoutView,
    LandingView,
)
from .apps import UserConfig

app_name = UserConfig.name

urlpatterns = [
    path("", LandingView.as_view(), name="landing"),
    path("login/", LoginView.as_view(), name="login"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
