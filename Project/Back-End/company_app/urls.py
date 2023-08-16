from django.urls import path, register_converter
from .views import A_Company, All_Companies
from .converters import IntOrStrConverter

register_converter(IntOrStrConverter,'int_or_str')
urlpatterns = [
    # Search for all companies
    path("", All_Companies.as_view(), name="all_companies"),
    # Search for a company by name or ID
    path("<int_or_str:name_or_id>/", A_Company.as_view(), name="a_company")
]