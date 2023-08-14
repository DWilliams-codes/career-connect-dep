from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Skill
from .serializers import SkillSerializer
# Create your views here.
class All_Skills(APIView):
    def get(self, request):
        skills = SkillSerializer(Skill.objects.all(), many = True)
        return Response(skills.data)
class A_Skill(APIView):
    def get(self, request, name):
        skill = SkillSerializer(get_object_or_404(Skill, name = name)).data
        return Response(skill)