from rest_framework.serializers import ModelSerializer
from .models import Job_Posting

class Job_PostingSerializer(ModelSerializer):

    class Meta:
        model = Job_Posting
        fields = ["__all__".lower()]