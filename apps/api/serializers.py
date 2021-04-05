from django.urls import path, include
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from apps.employees.models import Employee


# Serializers define the API representation.
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['name', 'departments', 'company']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['name']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_staff']
