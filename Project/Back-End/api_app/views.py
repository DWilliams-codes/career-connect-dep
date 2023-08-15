from django.shortcuts import render
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
import pprint
# Create your views here.
# Ask about best way to intergrate data from Adzuna APIs
pp = pprint.PrettyPrinter(indent=2)
app_id = "4b14710d"
api_key = "0fb491faea64ffec4a826d11877899b1"
class Azunda(APIView):
    def get(self, request, **parmaters):
        endpoint = f"https://api.adzuna.com/v1/api/jobs/us/search/1?app_id={app_id}d&app_key={api_key}"+parmaters
        response = requests.get(endpoint)
        pp.pprint(response)
        return Response(response)