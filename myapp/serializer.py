from rest_framework import serializers

from .models import Task, TaskTracker


class SerForm1(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class SerForm2(serializers.ModelSerializer):
    class Meta:
        model = TaskTracker
        fields = '__all__'
