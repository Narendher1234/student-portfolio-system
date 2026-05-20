from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Teacher


@api_view(['POST'])
def teacher_login(request):

    username = request.data.get("username")
    password = request.data.get("password")

    try:
        teacher = Teacher.objects.get(username=username, password=password)

        return Response({
            "message": "Login Success",
            "id": teacher.id,
            "username": teacher.username,
            "role": teacher.role
        })

    except Teacher.DoesNotExist:
        return Response({
            "error": "Invalid credentials"
        })