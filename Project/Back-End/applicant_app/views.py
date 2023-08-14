from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Applicant
from .serializers import ApplicantSerializer
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
# Create your views here.
class All_Applicants(APIView):
    def get(self,request):
        applicants = ApplicantSerializer(Applicant.objects.all().order_by("name"), many = True)
        return Response(applicants.data, status=HTTP_200_OK)
class A_Applicant(APIView):
    def get(self, request, id_or_name):
            try:
                if id_or_name.isnumeric():
                    applicant = ApplicantSerializer(get_object_or_404(Applicant, id = id_or_name))
                else:
                    applicant = ApplicantSerializer(Applicant.objects.filter(name = id_or_name), many = True)
                return Response(applicant.data,status=HTTP_200_OK)
            except:
                return Response("Invalid Applicant!",status=HTTP_400_BAD_REQUEST)
class Applicants_by_Education(APIView):
    def get(self,request, education_type):
        try:
            # applicants_by_education = Applicant.objects.filter(education["degree_type"]=education_type)
           applicants = ApplicantSerializer(Applicant.objects.all(),many = True)
           applicant_list = []
           for applicant in applicants:
               if applicant["education"]["degree_type"] == education_type:
                    applicant_list.append(applicant.data)
                    return Response(applicant_list, status=HTTP_200_OK)
        except:
           return Response("Invalid Applicant!",status=HTTP_400_BAD_REQUEST)
class Applicants_by_Skills(APIView):
    def get(self, request, skill):
         try:
           applicants = ApplicantSerializer(Applicant.objects.all(),many = True)
           applicant_list = []
           for applicant in applicants:
               if applicant["skill"].includes(skill):
                    applicant_list.append(applicant.data)
                    return Response(applicant_list, status=HTTP_200_OK)
         except:
           return Response("Invalid Applicant!",status=HTTP_400_BAD_REQUEST)
class A_Applicant_by_email(APIView):
    def get(self, request, email):
        try:
            applicant = ApplicantSerializer(get_object_or_404(Applicant, email = email)).data
            return Response(applicant,status=HTTP_200_OK)
        except:
            return Response("Invalid Applicant!",status=HTTP_400_BAD_REQUEST)