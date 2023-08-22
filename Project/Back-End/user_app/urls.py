from django.urls import path
from .views import Log_In, Log_Out, Sign_Up, Info

urlpatterns = [
    path("", Info.as_view()),
    path("sign-up/", Sign_Up.as_view()),
    path("sign-in/", Log_In.as_view()),
    path('log-out/', Log_Out.as_view()),
]