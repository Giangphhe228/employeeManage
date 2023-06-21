from django.urls import path
from .views import ManagerViewSet

 
urlpatterns = [
    path("get-manager/", ManagerViewSet.as_view()),
]