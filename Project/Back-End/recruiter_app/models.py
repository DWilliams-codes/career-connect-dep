from django.db import models
from user_app.models import User
from company_app.models import Company
from job_posting_app.models import Job_Posting
from applicant_app.models import Applicant

# Create your models here.
class Recruiter(models.Model):
    email = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    job_posting = models.ForeignKey(Job_Posting, on_delete=models.CASCADE)
    favorites = models.ForeignKey(Applicant, on_delete=models.CASCADE)