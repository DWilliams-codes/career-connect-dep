from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Education
from .serializers import EducationSerializer
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
# Create your views here.
class All_Education(APIView):
    def get(self, request):
        all_education = EducationSerializer(Education.objects.all().order_by("school_name"), many = True)
        return Response(all_education.data,status=HTTP_200_OK)
class Education_by_School(APIView):
    def get(self, request, school_name):
        try:
            education_by_school = Education.objects.filter(school_name=school_name).values()
            return Response(education_by_school,status=HTTP_200_OK)
        except:
            return Response("Invalid School",status=HTTP_400_BAD_REQUEST)
class Education_by_field(APIView):
    def get(self, request, degree_field):
        try:
            education_by_field = Education.objects.filter(degree_field=degree_field).values()
            return Response(education_by_field,status=HTTP_200_OK)
        except:
            return Response("Invalid Degree Field",status=HTTP_400_BAD_REQUEST)
class Education_by_degree(APIView):
    def get(self, request, degree_type):
        try:
            education_by_type = Education.objects.filter(degree_type=degree_type).values()
            return Response(education_by_type,status=HTTP_200_OK)
        except:
            return Response("Invalid Degree Type",status=HTTP_400_BAD_REQUEST)