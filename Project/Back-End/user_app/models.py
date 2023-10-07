from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, Group, Permission


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    name = models.CharField()
    account_type = models.CharField()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']
    groups = models.ManyToManyField(
        Group,
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="custom_user_groups",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="custom_user_permissions",
        related_query_name="user",
    )

    def __str__(self):
        return f"{self.email}"