from django.urls import path
from .views import Azunda

urlpatterns = [
    path('',Azunda.as_view(),name="azunda"),
]