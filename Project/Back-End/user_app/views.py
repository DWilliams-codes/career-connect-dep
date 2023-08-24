from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT, HTTP_200_OK
from applicant_app.models import Applicant
from recruiter_app.models import Recruiter
from company_app.models import Company

# Create your views here.
class Sign_Up(APIView):
    # Signs up users and creates respective account type, Refactor to Groups
    def post(self, request):
        # sets username to email
        request.data["username"] = request.data.get("email")
        company = Company.objects.get_or_create(name = request.data.get("company"))
        # create new user
        new_user = User.objects.create_user(**request.data)
        token = Token.objects.create(user = new_user)
        # create applicant or recruiter based on account type
        if new_user.account_type == "applicant":
            Applicant.objects.create(email = new_user)
        elif new_user.account_type == "recruiter":
            Recruiter.objects.create(email = new_user, company = company)
        return Response({"user": new_user.email, "account_type":new_user.account_type,"token":token.key}, status=HTTP_201_CREATED)
class Log_In(APIView):
    def post(self, request):
         # Authenticates the User an Logs them in
            print(request.data)
            user = authenticate(**request.data)
            if user:
                token, created = Token.objects.get_or_create(user = user)
                return Response({"token":token.key,"user":user.email}, status=HTTP_200_OK)
            else:
                 return Response("USER NOT SIGNED IN",status=HTTP_404_NOT_FOUND)
# Log Out user
class Log_Out(APIView):
    # Athenticates the User and Logs them out
        authentication_classes = [TokenAuthentication]
        permission_classes = [IsAuthenticated]
        def post(self, request):
            print(request)
            # deletes log in token
            try:
                    request.user.auth_token.delete()
                    return Response(status=HTTP_204_NO_CONTENT)
            except:
                    return Response("USER NOT SIGNED IN")
class Info(APIView):
    # Authenticates User and Returns email
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"email":request.user.email})