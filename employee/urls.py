from django.urls import path
from .views import EmpViewSet

 
urlpatterns = [
    path("get-employee/", EmpViewSet.as_view()),
]