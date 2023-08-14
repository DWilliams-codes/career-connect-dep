from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Education
from .serializers import EducationSerializer

# Create your views here.
class All_Education(APIView):
    def get(self, request):
        all_education = EducationSerializer(Education.objects.all(), many = True)
        return Response(all_education.data)
class Education_by_School(APIView):
    def get(self, request, school_name):
        education_by_school = Education.objects.filter(school_name=school_name).values()
        return Response(education_by_school)
class Education_by_field(APIView):
    def get(self, request, degree_field):
        education_by_field = Education.objects.filter(degree_field=degree_field).values()
        return Response(education_by_field)
class Education_by_degree(APIView):
    def get(self, request, degree_type):
        education_by_type = Education.objects.filter(degree_type=degree_type).values()
        return Response(education_by_type)