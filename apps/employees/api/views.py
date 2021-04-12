from rest_framework import viewsets
from apps.employees.models import Employee
from .serializers import EmployeeSerializer


# API
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
