from rest_framework.serializers import ModelSerializer
from .models import Job_Posting

class Job_PostingSerializer(ModelSerializer):

    class Meta:
        model = Job_Posting
        fields = ["title".lower(), "job_type".lower(), "job_description", "degree_type".lower(),"skill","salary","location","applicants","company", "recruiter"]