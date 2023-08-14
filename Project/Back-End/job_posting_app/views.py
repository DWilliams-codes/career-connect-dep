from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import Job_PostingSerializer, Job_Posting
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK

# Create your views here.
class All_Job_Postings(APIView):
    def get(self, request):
        job = Job_PostingSerializer(Job_Posting.objects.all().order_by("title"), many = True)
        return Response(job.data)
class A_Job_Posting(APIView):
    def get(self, request, id_or_title):
        try:
            if id_or_title.isnumeric():
                job_posting = Job_PostingSerializer(get_object_or_404(Job_Posting, id = id_or_title))
            else:
                job_posting = Job_PostingSerializer(get_object_or_404(Job_Posting, title = id_or_title))
            return Response(job_posting.data,status=HTTP_200_OK)
        except:
            return Response("Invalid Job Posting!",status=HTTP_400_BAD_REQUEST)
class Job_Postings_by_Skills(APIView):
    def get(self, request, job_skills):
        try:
            jobs = Job_PostingSerializer(Job_Posting.objects.all(), many = True)
            job_res = []
            for job in jobs:
                job_by_skill = job["skill"]["name"].includes(job_skills)
                job_res.append(job_by_skill.data)
            return Response(job_res,status=HTTP_200_OK)
        except:
            return Response("Invalid Job Posting!",status=HTTP_400_BAD_REQUEST)
class Job_Postings_by_Education(APIView):
    def get(self, request, request_education):
        try:
            job_postings_by_education = Job_Posting.objects.filter(degree_type = request_education).values()
            return Response(job_postings_by_education,status=HTTP_200_OK)
        except:
            return Response("Invalid Job Posting!",status=HTTP_400_BAD_REQUEST)
class Job_Postings_by_Company(APIView):
    def get(self, request, request_company):
        try:
            job_postings_by_company = Job_Posting.objects.filter(company = request_company).values()
            return Response(job_postings_by_company,status=HTTP_200_OK)
        except:
            return Response("Invalid Job Posting!",status=HTTP_400_BAD_REQUEST)
class Job_Postings_by_Type(APIView):
        def get(self, request, job_type):
            try:
                job_postings_by_type = Job_Posting.objects.filter(job_type=job_type).values()
                return Response(job_postings_by_type,status=HTTP_200_OK)
            except:
                return Response("Invalid Job Posting!",status=HTTP_400_BAD_REQUEST)
class Job_Postings_by_location(APIView):
    def get(self, request, location):
        try:
            job_postings_by_location = Job_Posting.objects.filter(location = location)
            return Response(job_postings_by_location,status=HTTP_200_OK)
        except:
            return Response("Invalid Job Posting!",status=HTTP_400_BAD_REQUEST)
