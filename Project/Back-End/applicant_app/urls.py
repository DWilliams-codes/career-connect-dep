from django.urls import path, register_converter
from .views import All_Applicants, A_Applicant,A_Applicant_by_email,Applicants_by_Education,Applicants_by_Skills
from .converters import IntOrStrConverter

register_converter(IntOrStrConverter, 'int_or_str')
urlpatterns = [
    path("", All_Applicants.as_view(), name="all_applicants"),
    path("<int_or_str:id_or_name>/", A_Applicant.as_view(), name="a_applicant"),
    path("education/<str:education_type>/", Applicants_by_Education.as_view(),name="applicants_by_education"),
    path("skills/<str:skill>/",Applicants_by_Skills.as_view(),name="applicants_by_skills"),
    path("email/<str:email>/", A_Applicant_by_email.as_view(),name="applicant_by_email"),
]