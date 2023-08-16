from django.shortcuts import render
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
import pprint
from datetime import datetime
# Create your views here.
# Ask about best way to intergrate data from Adzuna APIs
pp = pprint.PrettyPrinter(indent=2)
app_id = "4b14710d"
api_key = "0fb491faea64ffec4a826d11877899b1"
class Adzuna(APIView):
    def get_jobs(parmaters):
        # Testing API Calls
        endpoint = f"https://api.adzuna.com/v1/api/jobs/us/search/1?app_id={app_id}&app_key={api_key}{parmaters}&results_per_page=100"
        response = requests.get(endpoint)
        jsonresponse = response.json()
        # pp.pprint(jsonresponse)
        job_list = []
        total = round(len(jsonresponse.get("results"))/2)
        for jobs_num in range(total):
            date = jsonresponse.get("results")[jobs_num]["created"]
            year = int(date.split("-")[0])
            current_year = datetime.now()
            if year < current_year.year:
                continue
            id = jsonresponse.get("results")[jobs_num]["id"]
            title = jsonresponse.get("results")[jobs_num]["title"]
            description = jsonresponse.get("results")[jobs_num]["description"]
            salary = jsonresponse.get("results")[jobs_num]["salary_max"]
            location = jsonresponse.get("results")[jobs_num]["location"]["display_name"]
            # city = location.split(",")[0]
            company = jsonresponse.get("results")[jobs_num]["company"]["display_name"]
            recruiter = "Adzuna"
            job_dict = {"id":id,"title":title,"descrition":description,"salary":salary,"location":location,"company":company,"recruiter":recruiter}
            job_list.append(job_dict)
        return job_list