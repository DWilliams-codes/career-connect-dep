from rest_framework.serializers import ModelSerializer
from .models import Job_Posting

class Job_PostingSerializer(ModelSerializer):
    
    class Meta:
        model = Job_Posting
        fields = ["id","title", "job_type", "job_description", "degree_type","skill","salary","location","applicants","company", "recruiter"]