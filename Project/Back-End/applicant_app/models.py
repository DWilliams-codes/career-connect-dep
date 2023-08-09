from django.db import models
from education_app.models import Education
from skills_app.models import Skill
from job_posting_app.models import Job_Posting
from user_app.models import User
# Create your models here.
class Applicant(models.Model):
    email = models.OneToOneField(User, on_delete=models.CASCADE)
    education = models.ManyToManyField(Education, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill, on_delete=models.CASCADE)
    favorites = models.ManyToManyField(Job_Posting, on_delete=models.CASCADE)
