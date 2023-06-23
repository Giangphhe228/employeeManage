from django.urls import path
from .views import RoleViewSet

 
urlpatterns = [
    path("get-role/", RoleViewSet.as_view())
]