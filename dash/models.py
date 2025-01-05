from django.db import models
from django.contrib.auth.models import AbstractUser
from encrypted_model_fields.fields import EncryptedCharField
 
class User(AbstractUser):
    pass


class PasswordEntry(models.Model):
    mycat = (
        ('youtube','YOUTUBE'),
        ('gmail','GMAIL'),
        ('other','OTHER'),
    )
    category = models.CharField(choices=mycat, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="password_entries")
    site_name = models.CharField(max_length=255)
    site_url = models.URLField()
    username = models.CharField(max_length=255)
    encrypted_password = EncryptedCharField(max_length=500)
    remarks = models.TextField(blank=True, null=True)
