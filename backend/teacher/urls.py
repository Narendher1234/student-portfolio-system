from django.urls import path
from .views import teacher_login

urlpatterns = [
    path("teacher-login/", teacher_login),
]