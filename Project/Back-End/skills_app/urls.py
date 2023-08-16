from django.urls import path
from .views import A_Skill, All_Skills

urlpatterns = [
    # Returns all skills
    path("",All_Skills.as_view(), name="all_skills"),
    # Returns an individual skill by name
    path("<str:name>/",A_Skill.as_view(), name="a_skill"),
]