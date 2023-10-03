from django.shortcuts import render
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
import pprint
from datetime import datetime
from job_posting_app.models import Job_Posting
from job_posting_app.serializers import Job_PostingSerializer
from dotenv import load_dotenv
import os
# Create your views here.
# Refactor to Grab Multiple Pages of Data
pp = pprint.PrettyPrinter(indent=2)
api_key = os.environ.get("api_key")
app_id = os.environ.get("app_id")
# I would break this function up a bit and follow the Single Responsibility Principle to isolate behavior and help debugging later on in your projects life
class Adzuna(APIView):
    def get_jobs(parameters=" "):
        try:
            # API Call
            endpoint = f"https://api.adzuna.com/v1/api/jobs/us/search/1?app_id={app_id}&app_key={api_key}{parameters}&results_per_page=50"
            response = requests.get(endpoint)
            jsonresponse = response.json()
            # API Serializer?
            job_list = []
            # Number of Jobs on the Returned page
            total = round(len(jsonresponse.get("results"))/2)
            # print(total)
            # loops through all the jobs on the page
            for jobs_num in range(total):
                id = jsonresponse.get("results")[jobs_num]["id"]
                title = jsonresponse.get("results")[jobs_num]["title"]
                description = jsonresponse.get("results")[jobs_num]["description"]
                salary = jsonresponse.get("results")[jobs_num]["salary_max"]
                state = jsonresponse.get("results")[jobs_num]["location"]["area"][1]
                city = jsonresponse.get("results")[jobs_num]["location"]["area"][-1]
                location = f"{city},{state}"
                company = jsonresponse.get("results")[jobs_num]["company"]["display_name"]
                recruiter = "Adzuna" # Adzuna doesn't have specific recruiters so all jobs will be given this default
                # Grab copy from local database or create posting, so it can be moved around in backend 
                # get or create job posting
                job_dict = {"id":id,"title":title,"job_description":description,"salary":salary,"location":location,"company":company,"recruiter":recruiter}
                # job_dict = Job_PostingSerializer(Job_Posting.objects.get_or_create(id=id,title=title,description=description,salary=salary,location=location,company=company,recruiter=recruiter), many = True).data
                # job_posting_object = Job_PostingSerializer(Job_Posting.objects.get_or_create(job_dict)).data
                # print(job_posting_object)
                job_list.append(job_dict)
                # list of all Job postings in the current year
            return job_list
        except Exception as e:
            print(e)
            return([])
    def get_companies(parameters=" "):
        pass