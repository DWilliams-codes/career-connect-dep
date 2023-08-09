from django.db import models

# Create your models here.
class Address(models.Model):
    street = models.CharField(null=False)
    city = models.CharField(null=False)
    state = models.CharField(null=False)
    zip = models.BigIntegerField(null=False)
