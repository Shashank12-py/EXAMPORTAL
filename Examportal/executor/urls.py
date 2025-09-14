from django.urls import path
from .views import execute_code

urlpatterns = [
    path("run/", execute_code, name="execute_code"),
]
