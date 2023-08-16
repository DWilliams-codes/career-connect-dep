from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Recruiter
from .serializers import RecruiterSerializer
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK

# Create your views here.
# Return All Recruiters
class All_Recruiters(APIView):
    def get(self, request):
        recruiters = RecruiterSerializer(Recruiter.objects.all(), many = True)
        return Response(recruiters.data,status=HTTP_200_OK)
# Return a specific recruiter by id or all recruiters with that name
class A_Recruiter(APIView):
    def get(self, request, id_or_name):
        try:
            if id_or_name.isnumeric():
                recruiter = RecruiterSerializer(get_object_or_404(Recruiter, id = id_or_name))
            else:
                recruiter = RecruiterSerializer(Recruiter.objects.filter(name = id_or_name))
            return Response(recruiter.data,status=HTTP_200_OK)
        except:
            return Response("Invalid Recruiter!",status=HTTP_400_BAD_REQUEST)
# Return recruiter by email
class A_Recruiter_by_email(APIView):
    def get(self, request, email):
        try:
            recruiter = RecruiterSerializer(get_object_or_404(Recruiter, email = email)).data
            return Response(recruiter,status=HTTP_200_OK)
        except:
            return Response("Invalid Recruiter!",status=HTTP_400_BAD_REQUEST)
# Return all recruiters at a specific company
class Recruiter_by_Company(APIView):
    def get(self, request, company):
        try:
            recruiters = Recruiter.objects.filter(company = company).values()
            return Response(recruiters,status=HTTP_200_OK)
        except:
            return Response("Invalid Recruiter!",status=HTTP_400_BAD_REQUEST)