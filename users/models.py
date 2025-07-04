from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    ROLES = [
        ('user', "User"),
        ('admin', "Admin"),
    ]
    role = models.CharField(max_length=12, choices=ROLES, default='user')