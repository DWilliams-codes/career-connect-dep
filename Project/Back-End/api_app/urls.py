from django.urls import path
from .views import Adzuna

urlpatterns = [
    # pings adzuna api for search
    path('', Adzuna.as_view(),name="adzuna"),
]