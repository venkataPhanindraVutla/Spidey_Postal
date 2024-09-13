from django.db import models

# Create your models here.
class Stamp(models.Model):
    image_url = models.CharField(max_length=500)
    postal_circle = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField()
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    
class Order(models.Model):
    stamp = models.ForeignKey(Stamp, blank=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 