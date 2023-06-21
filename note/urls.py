from django.urls import path
from .views import NoteViewSet

 
urlpatterns = [
    path("get-note/", NoteViewSet.as_view())
]