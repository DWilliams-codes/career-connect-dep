from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Applicant
from .serializers import ApplicantSerializer

# Create your views here.
class All_Applicants(APIView):
    def get(self,request):
        applicants = ApplicantSerializer(Applicant.objects.all().order_by("name"), many = True)
        return Response(applicants.data)
class A_Applicant(APIView):
    def get(self, request, id_or_name):
            if id_or_name.isnumeric():
                applicant = ApplicantSerializer(get_object_or_404(Applicant, id = id_or_name))
            else:
                applicant = ApplicantSerializer(Applicant.objects.filter(name = id_or_name), many = True)
            return Response(applicant.data)
class Applicants_by_Education(APIView):
    def get(self,request, education_type):
        pass
        # applicants = Applicant.objects.filter(education["degree_type"] = education_type).values()
        # return Response(applicants)
class Applicants_by_Skills(APIView):
    pass
class A_Applicant_by_email(APIView):
    def get(self, request, email):
        applicant = ApplicantSerializer(get_object_or_404(Applicant, email = email)).data
        return Response(applicant)