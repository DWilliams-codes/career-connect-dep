from django.urls import path, register_converter
from .views import All_Applicants, A_Applicant,Applicants_by_Education,Applicants_by_Skills
from .converters import IntOrStrConverter

register_converter(IntOrStrConverter, 'int_or_str')
urlpatterns = [
    # Searches all applicants
    path("", All_Applicants.as_view(), name="all_applicants"),
    # Serch applicants by name or id
    path("<int_or_str:id_or_email>/", A_Applicant.as_view(), name="a_applicant"),
    # Search applicants by education
    path("education/<str:education_type>/", Applicants_by_Education.as_view(),name="applicants_by_education"),
    # Search applicants by skill
    path("skills/<str:skill>/",Applicants_by_Skills.as_view(),name="applicants_by_skills"),
]