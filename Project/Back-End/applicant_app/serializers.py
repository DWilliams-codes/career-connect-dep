from rest_framework.serializers import ModelSerializer
from .models import Applicant

class ApplicantSerializer(ModelSerializer):

    class Meta:
        model = Applicant
        fields = ["__all__"]