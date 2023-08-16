from django.urls import path
from .views import Education_by_degree, Education_by_field, Education_by_School, All_Education

urlpatterns = [
    # Returns All Educational institutions 
    path("", All_Education.as_view(), name="all_education"),
    # Searches for all education under a specific school
    path("school/<str:school_name>/", Education_by_School.as_view(), name="education_by_school"),
    # Searches for all educations with a specific field
    path("field/<str:degree_field>/", Education_by_field.as_view(), name="education_by_field"),
    # Searches for all educations with a specific field
    path("degree/<str:degree_type>/", Education_by_degree.as_view(), name="education_by_degree"),
]