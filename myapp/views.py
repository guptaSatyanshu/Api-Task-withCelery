from django.shortcuts import render, HttpResponse
from myapp.tasks import send_email_task

# Create your views here.

from rest_framework import viewsets
from .serializer import SerForm1, SerForm2
from .models import Task, TaskTracker
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class SerForm1Views(viewsets.ModelViewSet):
    serializer_class = SerForm1
    queryset = Task.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class SerForm2Views(viewsets.ModelViewSet):
    serializer_class = SerForm2
    queryset = TaskTracker.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]


def celerymail(request):
    send_email_task.delay(10)
    return HttpResponse('Email has been sent!!')
