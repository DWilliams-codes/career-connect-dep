from django.db import models
from skills_app.models import Skill
from recruiter_app.models import Recruiter

# Create your models here.
class Job_Posting(models.Model):
    title = models.CharField()
    job_type = models.CharField()
    job_description = models.CharField()
    skill = models.ManyToManyField(Skill, on_delete=models.CASCADE)
    salary_range = models.BigIntegerField()
    location = models.CharField()
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE)