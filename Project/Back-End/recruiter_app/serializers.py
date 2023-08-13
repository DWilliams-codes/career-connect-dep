from rest_framework.serializers import ModelSerializer
from .models import Recruiter

class RecruiterSerializer(ModelSerializer):

    class Meta:
        model = Recruiter
        fields = ["__all__"]