from django.urls import path
from .views import PerViewSet

 
urlpatterns = [
    path("get-per/", PerViewSet.as_view())
]