from django.db import models
from skills_app.models import Skill

# Create your models here.
class Job_Posting(models.Model):
    title = models.CharField()
    job_type = models.CharField()
    job_description = models.CharField()
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    salary_range = models.BigIntegerField()
    location = models.CharField()