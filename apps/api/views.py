from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from apps.employees.models import Employee
from .serializers import EmployeeSerializer, GroupSerializer, UserSerializer
# Create your views here.


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
