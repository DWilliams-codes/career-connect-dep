from django.shortcuts import render
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
import pprint
from datetime import datetime
from personal_project_env.api_keys import api_key, app_id
# Create your views here.
# Ask about best way to intergrate data from Adzuna APIs
# Refactor to Grab Multiple Pages of Data
pp = pprint.PrettyPrinter(indent=2)
# I would break this function up a bit and follow the Single Responsibility Principle to isolate behavior and help debugging later on in your projects life
class Adzuna(APIView):
    def get_jobs(parameters=" "):
        try:
            # API Call
            endpoint = f"https://api.adzuna.com/v1/api/jobs/us/search/1?app_id={app_id}&app_key={api_key}{parameters}&results_per_page=50"
            response = requests.get(endpoint)
            jsonresponse = response.json()
            # pp.pprint(jsonresponse)
            # API Serializer?
            job_list = []
            # Number of Jobs on the Returned page
            total = round(len(jsonresponse.get("results"))/2)
            print(total)
            # loops through all the jobs on the page
            for jobs_num in range(total):
                # Date the job was posted
                date = jsonresponse.get("results")[jobs_num]["created"]
                year = int(date.split("-")[0])
                current_year = datetime.now()
                # Return only Job postings from the current Year
                # Need to write better logic for the first month of the year
                # If january decrease current year
                if year < current_year.year:
                    continue
                id = jsonresponse.get("results")[jobs_num]["id"]
                title = jsonresponse.get("results")[jobs_num]["title"]
                description = jsonresponse.get("results")[jobs_num]["description"]
                salary = jsonresponse.get("results")[jobs_num]["salary_max"]
                location = jsonresponse.get("results")[jobs_num]["location"]["display_name"]
                # city = location.split(",")[0]
                company = jsonresponse.get("results")[jobs_num]["company"]["display_name"]
                recruiter = "Adzuna" # Adzuna doesn't have specific recruiters so all jobs will be given this default
                # Dict object to add to return
                job_dict = {"id":id,"title":title,"description":description,"salary":salary,"location":location,"company":company,"recruiter":recruiter}
                job_list.append(job_dict)
                # list of all Job postings in the current year
            return job_list
        except:
            return([])
    def get_companies(parameters=" "):
        pass