from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Applicant
from .serializers import ApplicantSerializer
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
import json
# Create your views here.
# Returns All applicants
class All_Applicants(APIView):
    def get(self,request):
        applicants = ApplicantSerializer(Applicant.objects.all().order_by("id"), many = True)
        print(applicants.data)
        return Response(applicants.data, status=HTTP_200_OK)
# Returns a specific applicant by name
class A_Applicant(APIView):
    def get(self, request, id_or_email):
            # searches through database of applicants by name or id
            try:
                print(id_or_email)
                applicant = Applicant.objects.get(id = id_or_email)
                if applicant:
                    serialized_applicant = ApplicantSerializer(applicant)
                else:
                        serialized_applicant = ApplicantSerializer(Applicant.objects.filter(email= id_or_email), many = True).data
                return Response(serialized_applicant,status=HTTP_200_OK)
            except Exception as e:
                print(e)
                return Response("Invalid Applicant!",status=HTTP_400_BAD_REQUEST)
# Returns all applicants with a specifc degree type (Bachelors, Associates, Masters, PHD)
class Applicants_by_Education(APIView):
    def get(self,request, education_type):
        try:
            # Searches through all applicants by degree type
            applicants = ApplicantSerializer(Applicant.objects.all(),many = True)
            # empty list to hold applicants
            applicant_list = []
            # loops through all applicants with specific degree under education
            for applicant in applicants:
                if applicant["education"]["degree_type"] == education_type:
                    applicant_list.append(applicant.data)
            return Response(applicant_list, status=HTTP_200_OK)
        except:
           return Response("Invalid Applicant!",status=HTTP_400_BAD_REQUEST)
# Returns all applicants with specific skill
class Applicants_by_Skills(APIView):
    def get(self, request, skill):
         try:
            # loops through applicant that have a specific skill
            applicants = ApplicantSerializer(Applicant.objects.all(),many = True)
            applicant_list = []
            for applicant in applicants:
               # check if applicant has skill and adds to list
               if skill in applicant.get("skill"):
                    applicant_list.append(applicant.data)
            return Response(applicant_list, status=HTTP_200_OK)
         except:
           return Response("Invalid Applicant!",status=HTTP_400_BAD_REQUEST)
