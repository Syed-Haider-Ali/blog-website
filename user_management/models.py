import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    guid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    REQUIRED_FIELDS = ["email", "password"]

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
