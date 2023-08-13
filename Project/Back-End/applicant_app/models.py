from django.db import models
from education_app.models import Education
from skills_app.models import Skill
from job_posting_app.models import Job_Posting
from user_app.models import User
# Create your models here.
class Applicant(models.Model):
    email = models.OneToOneField(User, on_delete=models.CASCADE)
    education = models.ForeignKey(Education,default=None, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill, default=None, related_name="applicants")
    favorites = models.ManyToManyField(Job_Posting,default=None, related_name="applicants")
    # Recruiters = Recruiter many to many favorites (Not Working Yet)
