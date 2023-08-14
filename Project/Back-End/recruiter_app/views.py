from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Recruiter
from .serializers import RecruiterSerializer

# Create your views here.
class All_Recruiters(APIView):
    def get(self, request):
        recruiters = RecruiterSerializer(Recruiter.objects.all(), many = True)
        return Response(recruiters.data)
class A_Recruiter(APIView):
    def get(self, request, id_or_name):
        if id_or_name.isnumeric():
            recruiter = RecruiterSerializer(get_object_or_404(Recruiter, id = id_or_name)).data
        else:
            recruiter = Recruiter.objects.filter(name = id_or_name).values()
        return Response(recruiter)
class A_Recruiter_by_email(APIView):
    def get(self, request, email):
        recruiter = RecruiterSerializer(get_object_or_404(Recruiter, email = email)).data
        return Response(recruiter)
class Recruiter_by_Company(APIView):
    def get(self, request, company):
        recruiters = Recruiter.objects.filter(company = company).values()
        return Response(recruiters)