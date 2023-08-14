from django.urls import path, register_converter
from .views import All_Job_Postings, A_Job_Posting, Job_Postings_by_Company, Job_Postings_by_Education, Job_Postings_by_location, Job_Postings_by_Skills, Job_Postings_by_Type
from .converters import IntOrStrConverter

register_converter(IntOrStrConverter, 'int_or_str')
urlpatterns = [
    path("", All_Job_Postings.as_view(), name="all_job_postings"),
    path("<int_or_str:id_or_title>/",A_Job_Posting.as_view(), name="a_job_posting"),
    path("skill/<str:job_skill>/",Job_Postings_by_Skills.as_view(), name="jobs_by_skill"),
    path("education/<str:education>/",Job_Postings_by_Education.as_view(),name="jobs_by_education"),
    path("company/<str:company>/", Job_Postings_by_Company.as_view(), name="jobs_by_company"),
    path("type/<str:type>/", Job_Postings_by_Type.as_view(), name="job_by_type"),
    path("location/<str:location>/", Job_Postings_by_location.as_view(), name="job_by_location"),
]