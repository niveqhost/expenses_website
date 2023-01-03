from django.db import models

# Create your models here.
class CustomUser(models.Model):
    username = models.CharField(max_length=255)
    raw_password = models.CharField(max_length=255)
    email = models.TextField()

    class Meta:
        verbose_name = ' Custom User'
        verbose_name_plural = ' Custom Users'