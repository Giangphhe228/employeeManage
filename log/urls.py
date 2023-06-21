from django.urls import path
from .views import FormulaViewSet

 
urlpatterns = [
    path("get-formula/", FormulaViewSet.as_view())
]