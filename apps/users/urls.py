from django.urls import path
from apps.users.api_endpoints import RegisterUserView, LoginView, VerifyEmailView, ResetPasswordRequestView, ResetPasswordView, UserUpdateView

urlpatterns = [
    path('auth/register/', RegisterUserView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path("auth/verify-email/", VerifyEmailView.as_view(), name="verify-email"),
    path("auth/reset/password/request/", ResetPasswordRequestView.as_view(), name="reset-password-request"),
    path("auth/reset/password/confirm/", ResetPasswordView.as_view(), name="reset-password-confirm"),
    path("auth/profile/edit/", UserUpdateView.as_view(), name="user-edit")
]
