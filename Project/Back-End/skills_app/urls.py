from django.urls import path
from .views import A_Skill, All_Skills

urlpatterns = [
    path("",All_Skills.as_view(), name="all_skills"),
    path("<str:name>/",A_Skill.as_view(), name="a_skill"),
]