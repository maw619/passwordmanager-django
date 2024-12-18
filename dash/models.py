from django.db import models
from django.contrib.auth.models import AbstractUser

 
class User(AbstractUser):
    pass


class PasswordEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="password_entries")
    site_name = models.CharField(max_length=255)
    site_url = models.URLField()
    username = models.CharField(max_length=255)
    encrypted_password = models.TextField()
    remarks = models.TextField(blank=True, null=True)
