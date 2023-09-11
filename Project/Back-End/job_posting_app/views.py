from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import Job_PostingSerializer, Job_Posting
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_201_CREATED,HTTP_401_UNAUTHORIZED
from api_app.views import Adzuna
import json
from company_app.models import Company
from recruiter_app.models import Recruiter
from skills_app.models import Skill
from applicant_app.models import Applicant
from user_app.models import User
# Create your views here.
# Refactor to ask for everything in one url request 
# Returns all job postings

class All_Job_Postings(APIView):
    def get(self, request):
        jobs = Job_PostingSerializer(Job_Posting.objects.all().order_by("title"), many = True).data
        #  adzuna_list = Job_PostingSerializer(Adzuna.get_jobs(), many=True).data
        adzuna_list = Adzuna.get_jobs()
        return Response(jobs+adzuna_list)
    def post(self, request):
        # authentication_classes = [TokenAuthentication]
        # permission_classes = [IsAuthenticated]
        try:
            # Set user
            job_posting_data = request.data
            # user = User.objects.get(request.user)
            user = request.user
            print(user)
            account_type = user.account_type
            recruiter = Recruiter.objects.get(email = user.email)
            company = recruiter.company
            skill = request.data.get("skills")
            skill_object = Skill.objects.get_or_create(name=skill)
            # Check users acount type
            # Only allows Recruiters to post Job-Postings
            if account_type == "recruiter":
                newjob = Job_PostingSerializer(Job_Posting.objects.create(**job_posting_data, recruiter = recruiter, company=company, skills=skill_object))
                return Response(newjob,status=HTTP_201_CREATED)
            else:
                return Response("You do not have access to post jobs!",status=HTTP_401_UNAUTHORIZED)
        except Exception as e:
                print(request.data)
                print(e)
                return Response("Job Creation Failed",status=HTTP_401_UNAUTHORIZED)
# Returns a job posting by id or title
class A_Job_Posting(APIView):
    def get(self, request, id_or_title):
        try:
            # Check if input is id or a title
                if type(id_or_title) == int:
                    job_posting = Job_PostingSerializer(Job_Posting.objects.get(id=id_or_title)).data
                if job_posting == None:
                    # Searches through jobs on local database
                    job_posting = Job_Posting.objects.filter(title = id_or_title).values_list()
                # If no job postings with that title set job_postings to empty list
                if job_posting == None:
                    job_posting=[]
                # Changes the value to fit the url
                if type(id_or_title) == 'str':
                    url_name = f'&what={id_or_title.replace(" ","%20")}'
                else:
                    url_name = id_or_title
                # Pings Adzuna api to get list of jobs
                adzuna_list = Adzuna.get_jobs(parameters=f"{url_name}")
                # Add job listing query set to adzuna list
                adzuna_list+=job_posting
                return Response(adzuna_list,status=HTTP_200_OK)
        except Exception as e:
            return Response(f"Invalid Job Posting {id_or_title}! Exception:{e}",status=HTTP_400_BAD_REQUEST)
    def put(self, request, job_posting_id):
        try:
            authentication_classes = [TokenAuthentication]
            permission_classes = [IsAuthenticated]
            # Set user
            user = request.user
            account_type = user.account_type
            recruiter = Recruiter.objects.get(email = user.email)
            company = recruiter.company
            title = request.data.get("title")
            skill = request.data.get("skills")
            skill_object = Skill.objects.filter(name=skill)
            degree_type = request.data.get("degree_type")
            salary = request.data.get("salary")
            applicants = request.data.get("applicants")
            applicant_object = Applicant.objects.filter(email=applicants)

            if account_type == "recruiter":
                newjob = Job_Posting.objects.get(id=job_posting_id)
                newjob.company = company
                newjob.title = title
                newjob.skill += skill_object
                newjob.degree_type = degree_type
                newjob.salary = salary
                newjob.applicants += applicant_object
                return Response(newjob,status=HTTP_201_CREATED)
            else:
                return Response("You do not have access to post jobs!",status=HTTP_401_UNAUTHORIZED)
        except:
                return Response("Job Update Failed",status=HTTP_401_UNAUTHORIZED)
            
# Returns all jobs with a specific skill
class Job_Postings_by_Skills(APIView):
    def get(self, request, job_skills):
        try:
            # Grabs All jobs
            jobs = Job_PostingSerializer(Job_Posting.objects.all(), many = True)
            job_res = []
            # Add jobs to list if they match skill
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
            # filters through degree by type (Associates, Bachelors, Masters, Phd)
            job_postings_by_education = Job_Posting.objects.filter(degree_type = request_education.lower()).values()
            return Response(job_postings_by_education,status=HTTP_200_OK)
        except:
            return Response("Invalid Job Posting!",status=HTTP_400_BAD_REQUEST)
# Returns all job postings by company
class Job_Postings_by_Company(APIView):
    def get(self, request, request_company):
        try:
            # filters through job posting from the company in local database
            job_postings_by_company = Job_Posting.objects.filter(company__name = request_company.lower()).values_list()
            # Changes company to fit url
            url_name = request_company.replace(" ","%20")
            # searches Adzuna database for Job-Posting by the company
            adzuna_list = Adzuna.get_jobs(parameters=f"&company={url_name}")
            # Combine adzuna job postings list with local list
            adzuna_list+=job_postings_by_company
            return Response(adzuna_list,status=HTTP_200_OK)
        except:
            return Response("Invalid Job Posting!",status=HTTP_400_BAD_REQUEST)
# returns all job postings by type (Full-Time, Part-Time, Contract)
class Job_Postings_by_Type(APIView):
        def get(self, request, job_type):
            try:
                # filter through Job Postings by type 
                job_postings_by_type = Job_Posting.objects.filter(job_type=job_type).values()
                return Response(job_postings_by_type,status=HTTP_200_OK)
            except:
                return Response("Invalid Job Posting!",status=HTTP_400_BAD_REQUEST)
# Returns job posting by specific city
class Job_Postings_by_location(APIView):
    def get(self, request, location):
        try:
            # filter through job postings by City, State
            job_postings_by_location = Job_Posting.objects.filter(location = location).values_list()
            url_location = location.replace(",","%2c")
            # searches through adzuna database for list of jobs at that location
            adzuna_list = Adzuna.get_jobs(parameters=f"&where={url_location}")
            # Combine adzuna job postings list with local list
            adzuna_list+=job_postings_by_location
            return Response(adzuna_list,status=HTTP_200_OK)
        except:
            return Response("Invalid Job Posting!",status=HTTP_400_BAD_REQUEST)

def urlfilter(unfilteredURL):
    return(unfilteredURL.replace(" ","%20"))
# class A_Job_Posting(APIView):
#     def get(self, request, id_or_title):
#         try:
#             # Check if input is id or a title
#             if id_or_title.isnumeric():
#                 job_posting = Job_PostingSerializer(get_object_or_404(Job_Posting, id = id_or_title)).data
#             else:
#                 # Searches through jobs on local database
#                 job_posting = Job_Posting.objects.filter(title = id_or_title).values_list()
#                 # If no job postings with that title set job_postings to empty list
#                 if job_posting == None:
#                     job_posting=[]
#                 # Changes the value to fit the url
#                 url_name = id_or_title.replace(" ","%20")
#                 # Pings Adzuna api to get list of jobs
#                 adzuna_list = Adzuna.get_jobs(parameters=f"&what={url_name}")
#                 # Add job listing query set to adzuna list
#                 adzuna_list+=job_posting
#             return Response(adzuna_list,status=HTTP_200_OK)