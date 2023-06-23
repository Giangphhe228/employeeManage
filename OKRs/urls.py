from django.urls import path
from .views import OkrViewSet

 
urlpatterns = [
    path("get-okr/", OkrViewSet.as_view()),
]