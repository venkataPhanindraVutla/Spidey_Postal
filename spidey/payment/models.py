from django.db import models
from base.models import Stamp

# Create your models here.

class Order(models.Model):
    stamp = models.ForeignKey(Stamp, blank=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=30, default="Pending")
    provider_order_id = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.stamp.__str__()
