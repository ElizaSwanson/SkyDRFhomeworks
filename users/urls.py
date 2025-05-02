from django.urls import path
from users.apps import UsersConfig
from users.views import PaymentList, UserCreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = UsersConfig.name

urlpatterns = [
    path("payments/", PaymentList.as_view(), name="payment-list"),
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
