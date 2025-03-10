from django.urls import path
from .views import (
    RegisterView, VerifyEmailView, LoginView, LogoutView,
    ResetPasswordRequestView, ResetPasswordView, UserUpdateView
)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("verify-email/", VerifyEmailView.as_view(), name="verify-email"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),

    # Parolni tiklash (2 bosqichli)
    path("reset-password/request/", ResetPasswordRequestView.as_view(), name="reset-password-request"),
    path("reset-password/confirm/", ResetPasswordView.as_view(), name="reset-password-confirm"),

    # Foydalanuvchi profilini tahrirlash
    path("edit-profile/", UserUpdateView.as_view(), name="edit-profile"),
    # path("profile-edit/", ProfileEditView.as_view(), name="profile-edit"),  # Yangi profil tahrirlash endpoint
]
