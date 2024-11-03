from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from .views import CustomTokenObtainPairView, LoginView, RegisterView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path(
        "api/token/refresh/", CustomTokenObtainPairView.as_view(), name="token_refresh"
    ),
]
