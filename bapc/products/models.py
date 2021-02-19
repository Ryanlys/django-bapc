from django.db import models

# Create your models here.
class Products(models.Model):
    tag = models.TextField(max_length=10)
    name = models.TextField(max_length=50)
    price = models.DecimalField(decimal_places=2,max_digits=7)
    expired = models.BooleanField(default=False)
    link = models.TextField(default="")