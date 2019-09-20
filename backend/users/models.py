from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    phonenum = models.CharField(max_length=100)
    finish_num = models.IntegerField(null=True, blank=True)
