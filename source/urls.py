from django.urls import path
from .views import SourceViewSet

 
urlpatterns = [
    path("get-source/", SourceViewSet.as_view())
]