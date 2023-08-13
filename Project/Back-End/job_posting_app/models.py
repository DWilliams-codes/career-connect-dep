from django.db import models
from skills_app.models import Skill
from recruiter_app.models import Recruiter
from company_app.models import Company
from applicant_app.models import Applicant

# Create your models here.
class Job_Posting(models.Model):
    title = models.CharField()
    job_type = models.CharField()
    job_description = models.CharField()
    skill = models.ManyToManyField(Skill,related_name="job_postings")
    salary_range = models.BigIntegerField()
    location = models.CharField()
    applicants = models.ManyToManyField(Applicant,default=None, related_name="favorites")
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE)