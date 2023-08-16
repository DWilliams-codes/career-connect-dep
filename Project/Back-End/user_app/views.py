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

# Create your views here.
# Signs up users and creates Respective account type, Refactor to Groups
class Sign_Up(APIView):
    def post(self, request):
        request.data["username"] = request.data.get("email")
        new_user = User.objects.create_user(**request.data)
        token = Token.objects.create(user = new_user)
        if new_user.account_type.lower() == "applicant":
            Applicant.objects.create(email = new_user)
        else:
            Recruiter.objects.create(email = new_user)
        return Response({"user": new_user.email, "account_type":new_user.account_type,"token":token.key}, status=HTTP_201_CREATED)
# Logs in User
class Log_In(APIView):
    def post(self, request):
        user = authenticate(**request.data)
        if user:
            token, created = Token.objects.get_or_create(user = user)
            return Response({"token":token.key,"user":user.email}, status=HTTP_200_OK)
        return Response("INVALID CREDENTIALS", status=HTTP_404_NOT_FOUND)
# Log Out user
class Log_Out(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=HTTP_204_NO_CONTENT)
# Return user email
class Info(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(request.user.email)