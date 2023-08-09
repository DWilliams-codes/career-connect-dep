from django.db import models
from address_app.models import Address

# Create your models here.
class Company(models.Model):
    company_name = models.CharField(null=False, unique=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)