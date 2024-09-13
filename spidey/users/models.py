from django.db import models
from django.contrib.auth.models import AbstractUser
from base.models import Order

class User(AbstractUser):
    orders = models.ManyToManyField(Order)
    address = models.TextField()

