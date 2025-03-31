from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from .utils import generate_code

class Role(models.Model):
    ROLE_CHOICES = [
        ("traveler", "Traveler"),
        ("partner", "Partner"),
        ("admin", "Admin"),
    ]

    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default="traveler", unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.role


class GenderChoices(models.TextChoices):
    MALE = "Male", "Male"
    FEMALE = "Female", "Female"
    OTHER = "Other", "Other"


class UserManager(BaseUserManager):
    def create_user(self, email, full_name, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)

        traveler_role, _ = Role.objects.get_or_create(role="traveler")
        extra_fields.setdefault("role", traveler_role)

        user = self.model(email=email, full_name=full_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, password=None, **extra_fields):
        admin_role, _ = Role.objects.get_or_create(role="admin")
        extra_fields.setdefault("role", admin_role)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, full_name, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=100, null=False)
    gender = models.CharField(max_length=10, choices=GenderChoices.choices, null=False)
    age = models.PositiveIntegerField(default=18)
    username = models.CharField(max_length=50, unique=True, blank=True, null=True)
    email = models.EmailField(unique=True, null=False)
    phone_number = models.CharField(max_length=15, unique=True, null=False)
    profile_photo = models.ImageField(upload_to="profile_photos/", blank=True, null=True)
    verification_code = models.CharField(max_length=6, blank=True, null=True)
    reset_password_code = models.CharField(max_length=6, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_verified = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True, default=None)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["full_name"]

    objects = UserManager()

    def save(self, *args, **kwargs):
        if not self.verification_code:
            self.email_verification_code = generate_code()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email