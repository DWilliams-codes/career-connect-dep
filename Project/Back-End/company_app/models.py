from django.db import models
from address_app.models import Address

# Create your models here.
class Company(models.Model):
    name = models.CharField(null=False, unique=True)
    address = models.ForeignKey(Address,default=None, on_delete=models.CASCADE)