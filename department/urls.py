from django.urls import path
from .views import DepartViewSet

 
urlpatterns = [
    path("get-depart/", DepartViewSet.as_view())
]