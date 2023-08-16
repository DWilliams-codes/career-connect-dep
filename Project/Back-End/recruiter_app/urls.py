from django.urls import path, register_converter
from .views import All_Recruiters, A_Recruiter_by_email,A_Recruiter, Recruiter_by_Company
from .converters import IntOrStrConverter

register_converter(IntOrStrConverter, 'int_or_str')
urlpatterns = [
    # Returns All recruiters
    path("", All_Recruiters.as_view(), name="all_All_recruiters"),
    # Returns a recruiter by name or ID
    path("<int_or_str:id_or_name>/", A_Recruiter.as_view(), name="a_recruiter"),
    # Returns a recruiter by email
    path("email/<str:email>/", A_Recruiter_by_email.as_view(),name="recruiter_by_email"),
    # Returns recruiters by Company
    path("company/<str:company>/", Recruiter_by_Company.as_view(),name="recruiter_by_company"),
]