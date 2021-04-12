from rest_framework import viewsets
from apps.employees.models import Employee
from .serializers import EmployeeSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


# API
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
