from django.db import models
from skills_app.models import Skill
from recruiter_app.models import Recruiter
from company_app.models import Company
from applicant_app.models import Applicant

# Create your models here.
class Job_Posting(models.Model):
    title = models.CharField()
    job_type = models.CharField(default="full-time")
    job_description = models.CharField()
    degree_type = models.CharField(default="none")
    skill = models.ManyToManyField(Skill,default=None,related_name="job_postings")
    salary = models.BigIntegerField()
    location = models.CharField() # City, State
    applicants = models.ManyToManyField(Applicant,default=None, related_name="favorites")
    company = models.ForeignKey(Company, on_delete=models.CASCADE,related_name="job_posting")
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE,related_name="job_posting")