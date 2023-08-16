from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Skill
from .serializers import SkillSerializer
from rest_framework.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_200_OK
# Create your views here.
# Return All skills
class All_Skills(APIView):
    def get(self, request):
        skills = SkillSerializer(Skill.objects.all().order_by("name"), many = True)
        return Response(skills.data)
# Return a specific skill by name
class A_Skill(APIView):
    def get(self, request, name):
        try:
            skill = SkillSerializer(get_object_or_404(Skill, name = name)).data
            return Response(skill)
        except:
            return Response("Invalid Skill",status=HTTP_400_BAD_REQUEST)