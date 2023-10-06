from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import Job_PostingSerializer, Job_Posting
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_201_CREATED,HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND
from api_app.views import Adzuna
import json
from company_app.models import Company
from recruiter_app.models import Recruiter
from skills_app.models import Skill
from applicant_app.models import Applicant
from user_app.models import User
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
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
            # get user object
            user = User.objects.get(email=job_posting_data["user"])
            # check if the user is a recruiter if yes returns user objects
            recruiter = Recruiter.objects.get(email = user)
            # set company for posting
            company = recruiter.company
            # set title
            title = job_posting_data.get("title")
            # set job type
            job_type = job_posting_data.get("job_type")
            # set job description
            job_description = job_posting_data.get("job_description")
            # set degree type
            degree_type = job_posting_data.get("degree_type")
            # grabs skill and set to skill objects
            skill = job_posting_data.get("skills","")
            skill_object = Skill.objects.get_or_create(name=skill)[0]
            # set salary
            salary = job_posting_data.get("salary")
            # set location
            location = job_posting_data.get("location")
            # Check users acount type
            # Only allows Recruiters to post Job-Postings
            if recruiter:
                newjob = Job_Posting.objects.create(title=title, job_type=job_type,job_description=job_description,degree_type=degree_type,salary=salary,location=location, recruiter=recruiter, company=company)
                newjob.skill.set([skill_object])
                serialized_newjob = Job_PostingSerializer(newjob).data
                return Response(serialized_newjob,status=HTTP_201_CREATED)
            else:
                return Response("You do not have access to post jobs!",status=HTTP_401_UNAUTHORIZED)
        except Exception as e:
                # print(job_posting_data)
                print(e)
                return Response("Job Creation Failed",status=HTTP_400_BAD_REQUEST)
# Returns a job posting by id or title
class A_Job_Posting(APIView):
    def get(self, request, **params):
        id_or_title = params["id_or_title"]
        try:
            location = params["location"]
        except:
            location = ""
        try: 
            # Check if input is id or a title
                job_posting = None
                if type(id_or_title) == int:
                    job_posting = Job_Posting.objects.filter(id=id_or_title).values_list()
                if job_posting == None:
                    # Searches through jobs on local database
                    job_posting = Job_Posting.objects.filter(title = id_or_title).values_list()
                # If no job postings with that title set job_postings to empty list
                if job_posting == None:
                    job_posting=[]
                # Changes the value to fit the url
                if type(id_or_title) == str:
                    url_name = f'&what={id_or_title.replace(" ","%20")}'
                    if location:
                        url_name+= f'&where={location.replace(" ","%20")}'
                # Pings Adzuna api to get list of jobs
                    adzuna_list = Adzuna.get_jobs(parameters=f"{url_name}")
                else:
                    adzuna_list = []
                # Add job listing query set to adzuna list
                adzuna_list+=job_posting
                return Response(adzuna_list,status=HTTP_200_OK)
        except Exception as e:
            return Response(f"Invalid Job Posting {id_or_title}! Exception:{e}",status=HTTP_400_BAD_REQUEST)
    def put(self, request, id_or_title):
        try:
            #refactor to keep applicants
            # authentication_classes = [TokenAuthentication]
            # permission_classes = [IsAuthenticated]
            # Set user
            job_posting_data = request.data
            # get user object
            user = User.objects.get(email=job_posting_data["user"])
            # check if the user is a recruiter if yes returns user objects
            recruiter = Recruiter.objects.get(email = user)
            # set company for posting
            company = recruiter.company
            # set title
            title = job_posting_data.get("title")
            # set job type
            job_type = job_posting_data.get("job_type")
            # set job description
            job_description = job_posting_data.get("job_description")
            degree_type = job_posting_data.get("degree_type")
            skill = job_posting_data.get("skills","")
            skill_object = Skill.objects.get_or_create(name=skill)[0]
            salary = job_posting_data.get("salary")
            location = job_posting_data.get("location")

            if recruiter:
                newjob = Job_Posting.objects.get(id=id_or_title)
                newjob.company = company
                newjob.title = title
                newjob.job_description = job_description
                newjob.job_type = job_type
                newjob.skill.set([skill_object])
                newjob.degree_type = degree_type
                newjob.salary = salary
                newjob.location = location
                serialized_newjob = Job_PostingSerializer(newjob).data
                return Response(serialized_newjob,status=HTTP_201_CREATED)
            else:
                return Response("You do not have access to post jobs!",status=HTTP_401_UNAUTHORIZED)
        except Exception as e:
                print(e)
                return Response("Job Update Failed",status=HTTP_400_BAD_REQUEST)
            
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
class Jobs_Favorites_List(APIView):
    def get(self, request):
        try:
            email = request.data
            print(email)
            try:
                recruiter_object = Recruiter.objects.get(email=email)
            except:
                applicant_object = Applicant.objects.get(email=email)
            if recruiter_object:
                jobs_data = Job_PostingSerializer(Job_Posting.objects.filter(recruiter = recruiter_object)).data
                return Response(jobs_data,status=HTTP_200_OK)
            else:
                jobs_data = Job_PostingSerializer(Job_Posting.objects.filter(applicants=applicant_object)).data
                return Response(jobs_data,status=HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response("Error returning jobs",status=HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def get_jobs_by_applicant(request, applicant_id):
    try:
        applicant = Applicant.objects.get(id=applicant_id)
        jobs = Job_Posting.objects.filter(applications__applicant=applicant)
        serialized_jobs = Job_PostingSerializer(jobs, many=True).data
        return Response(serialized_jobs, status=HTTP_200_OK)
    except Applicant.DoesNotExist:
        return Response({"error": "Applicant not found"}, status=HTTP_404_NOT_FOUND)
# for refactoring
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