from django.db import models

# Create your models here.
class Education(models.Model):
    school_name = models.CharField()
    degree_field = models.CharField()
    degree_type = models.CharField()
