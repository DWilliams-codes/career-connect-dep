from django.db import models
from user_app.models import User
from company_app.models import Company
from applicant_app.models import Applicant



# Create your models here.
class Recruiter(models.Model):
    email = models.OneToOneField(User.email, unique=True, on_delete=models.CASCADE)
    name = models.OneToOneField(User.name, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    # job_posting = models.ForeignKey(Job_Posting, on_delete=models.CASCADE)
    favorites = models.ManyToManyField(Applicant, default=None,related_name="Recruiters")