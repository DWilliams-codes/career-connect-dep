from rest_framework.serializers import ModelSerializer
from .models import Recruiter
from user_app.models import User

class RecruiterSerializer(ModelSerializer):
    name = User.name
    class Meta:
        model = Recruiter
        fields = ["email","name","company","favorites"]