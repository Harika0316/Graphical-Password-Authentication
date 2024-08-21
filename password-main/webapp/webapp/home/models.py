from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Password1(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img1 = models.CharField(max_length=200)
    img2 = models.CharField(max_length=200)
    img3 = models.CharField(max_length=200)
    img4 = models.CharField(max_length=200)
    img5 = models.CharField(max_length=200)