from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.core.validators import RegexValidator
from django.db.models.signals import pre_save

from user.constants import UserTypes, GenderTypes


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_active", extra_fields.get(
            "user_type") is UserTypes.PATIENT.value)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, email, username=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("user_type", UserTypes.ADMIN.value)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        if extra_fields.get("user_type") != UserTypes.ADMIN.value:
            raise ValueError("Superuser must have user_type=ADMIN.")
        return self._create_user(username, email, password, **extra_fields)


class CustomUser(AbstractUser):
    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",
        message="Phone number must be entered in the format: '+99999999'. Up to 15 digits allowed.",
    )
    email = models.EmailField(unique=True, blank=False)
    username = models.CharField(max_length=254, blank=True, null=True)
    user_type = models.CharField(
        max_length=20, choices=[(tag.value, tag.name) for tag in UserTypes]
    )
    phone_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=True, null=True
    )
    gender = models.CharField(
        max_length=14, choices=[(tag.value, tag.name) for tag in GenderTypes]
    )
    age = models.PositiveIntegerField(blank=True, null=True)

    objects = CustomUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['user_type', 'gender']

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.user_type}"

    def get_absolute_url(self):
        return f"/users/{self.pk}/"

    def get_email(self):
        return self.email