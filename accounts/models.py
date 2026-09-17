from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    is_business_owner = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)