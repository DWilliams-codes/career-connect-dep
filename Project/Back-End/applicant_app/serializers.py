from rest_framework.serializers import ModelSerializer
from .models import Applicant
from user_app.models import User
class ApplicantSerializer(ModelSerializer):
    name = User.name
    class Meta:
        model = Applicant
        fields = ["email","education","skills"]