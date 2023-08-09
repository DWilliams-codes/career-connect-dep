from django.db import models
from education_app.models import Education

# Create your models here.
class Applicant(models.Model):
    email = models.ForeignKey()
