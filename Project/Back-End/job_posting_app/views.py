from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import Job_PostingSerializer, Job_Posting
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from api_app.views import Adzuna
import json

# Create your views here.
# Returns all job postings
class All_Job_Postings(APIView):
    def get(self, request):
        jobs = Job_PostingSerializer(Job_Posting.objects.all().order_by("title"), many = True).data
        adzuna_list = Adzuna.get_jobs()
        return Response(jobs+adzuna_list)
# Returns a job posting by id or title
class A_Job_Posting(APIView):
    def get(self, request, id_or_title):
        try:
            if id_or_title.isnumeric():
                job_posting = Job_PostingSerializer(get_object_or_404(Job_Posting, id = id_or_title)).data
            else:
                job_posting = Job_Posting.objects.filter(title = id_or_title).values_list()
                if job_posting == None:
                    job_posting=[]
                url_name = id_or_title.replace(" ","%20")
                adzuna_list = Adzuna.get_jobs(parmaters=f"&what={url_name}")
                adzuna_list+=job_posting
            return Response(adzuna_list,status=HTTP_200_OK)
        except:
            return Response("Invalid Job Posting!",status=HTTP_400_BAD_REQUEST)
    def post(self, request, job_posting_data):
        authentication_classes = [TokenAuthentication]
        permission_classes = [IsAuthenticated]
        user = request.user
        if user.account_type.lower() == "recruiter":
            Job_Posting.objects.create(**job_posting_data)
        else:
            return Response("You do not have access to post jobs!",status=HTTP_400_BAD_REQUEST)
            
# Returns all jobs with a specific skill
class Job_Postings_by_Skills(APIView):
    def get(self, request, job_skills):
        try:
            jobs = Job_PostingSerializer(Job_Posting.objects.all(), many = True)
            job_res = []
            for job in jobs:
                if job["skills"]["name"] in job_skills:
                    job_by_skill = job["skill"]["name"]
                    job_res.append(job_by_skill.data)
            return Response(job_res,status=HTTP_200_OK)
        except:
            return Response("Invalid Job Posting!",status=HTTP_400_BAD_REQUEST)
# Returns all job postings with specific degree requirement
class Job_Postings_by_Education(APIView):
    def get(self, request, request_education):
        try:
            job_postings_by_education = Job_Posting.objects.filter(degree_type = request_education.lower()).values()
            return Response(job_postings_by_education,status=HTTP_200_OK)
        except:
            return Response("Invalid Job Posting!",status=HTTP_400_BAD_REQUEST)
# Returns all job postings by company
class Job_Postings_by_Company(APIView):
    def get(self, request, request_company):
        try:
            job_postings_by_company = Job_Posting.objects.filter(company__name = request_company.lower()).values_list()
            print(request_company)
            url_name = request_company.replace(" ","%20")
            adzuna_list = Adzuna.get_jobs(parmaters=f"&company={url_name}")
            adzuna_list+=job_postings_by_company
            return Response(adzuna_list,status=HTTP_200_OK)
        except:
            return Response("Invalid Job Posting!",status=HTTP_400_BAD_REQUEST)
# returns all job postings by type (Full-Time, Part-Time, Contract)
class Job_Postings_by_Type(APIView):
        def get(self, request, job_type):
            try:
                job_postings_by_type = Job_Posting.objects.filter(job_type=job_type).values()
                return Response(job_postings_by_type,status=HTTP_200_OK)
            except:
                return Response("Invalid Job Posting!",status=HTTP_400_BAD_REQUEST)
# Returns job posting by specific city
class Job_Postings_by_location(APIView):
    def get(self, request, location):
        try:
            job_postings_by_location = Job_Posting.objects.filter(location = location).values_list()
            url_location = location.replace(",","%2c")
            adzuna_list = Adzuna.get_jobs(parmaters=f"&where={url_location}")
            adzuna_list+=job_postings_by_location
            return Response(adzuna_list,status=HTTP_200_OK)
        except:
            return Response("Invalid Job Posting!",status=HTTP_400_BAD_REQUEST)
