from django.urls import path, register_converter
from .views import All_Job_Postings, A_Job_Posting, Job_Postings_by_Company, Job_Postings_by_Education, Job_Postings_by_location, Job_Postings_by_Skills, Job_Postings_by_Type
from .converters import IntOrStrConverter

register_converter(IntOrStrConverter, 'int_or_str')
urlpatterns = [
    # Returns All Job Postings
    path("", All_Job_Postings.as_view(), name="all_job_postings"),
    # Returns a job posting by ID or all job posting with that name, Post to create job postings
    path("<int_or_str:id_or_title>/",A_Job_Posting.as_view(), name="a_job_posting"),
    # return by search and location
     path("<int_or_str:id_or_title>/$where=<str:location>/",A_Job_Posting.as_view(), name="a_job_posting"),
    # Returns all job postings that have a specific skill
    path("skill/<str:job_skill>/",Job_Postings_by_Skills.as_view(), name="jobs_by_skill"),
    # Returns job posting with specific degree requirement
    path("education/<str:education>/",Job_Postings_by_Education.as_view(),name="jobs_by_education"),
    # Returns all job postings under a specific company
    path("company/<str:request_company>/", Job_Postings_by_Company.as_view(), name="jobs_by_company"),
    # Returns posting by job type (full-time,Part-time,Contract)
    path("type/<str:type>/", Job_Postings_by_Type.as_view(), name="job_by_type"),
    # Returns job postings in specific city
    path("location/<str:location>/", Job_Postings_by_location.as_view(), name="job_by_location"),
]