from django.db import models
from education_app.models import Education
from skills_app.models import Skill
from user_app.models import User
# Create your models here.
class Applicant(models.Model):
    email = models.OneToOneField(User.email, on_delete=models.CASCADE)
    name = models.OneToOneField(User.name, on_delete=models.CASCADE)
    education = models.ForeignKey(Education,default=None, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill, default=None, related_name="applicants")
    # Favorites = Job_posting many to many favorites
    # Recruiters = Recruiter many to many favorites
