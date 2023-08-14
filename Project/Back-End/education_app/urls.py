from django.urls import path
from .views import Education_by_degree, Education_by_field, Education_by_School, All_Education

urlpatterns = [
    path("", All_Education.as_view(), name="all_education"),
    path("school/<str:school_name>/", Education_by_School.as_view(), name="education_by_school"),
    path("field/<str:degree_field>/", Education_by_field.as_view(), name="education_by_field"),
    path("degree/<str:degree_type>/", Education_by_degree.as_view(), name="education_by_degree"),
]