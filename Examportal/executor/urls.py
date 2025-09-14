from django.urls import path
from .views import execute_code, index

urlpatterns = [
    path("run/", execute_code, name="execute_code"),
    path('', index, name='executor_index'),
]
