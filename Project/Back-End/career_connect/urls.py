"""
URL configuration for career_connect project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# refactor into one url

urlpatterns = [
    # Admin site
    path('admin/', admin.site.urls),
    # Job postings
    path('api/v1/job_postings/', include("job_posting_app.urls")),
    # Applicants
    path('api/v1/applicants/', include("applicant_app.urls")),
    # Recuiters
    path('api/v1/recruiters/', include("recruiter_app.urls")),
    # Companies
    path('api/v1/companies/', include("company_app.urls")),
    # Skills
    path('api/v1/skills/', include("skills_app.urls")),
    # Educations
    path('api/v1/education/', include("education_app.urls")),
    # Adzuna Third Party API
    path('api/v1/adzuna/', include("api_app.urls")),
    # Path for user authentication
    path("api/v1/users/", include("user_app.urls")),
]
