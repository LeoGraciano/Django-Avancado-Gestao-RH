
from rest_framework import serializers
from apps.employees.models import Employee


# Serializers define the API representation.
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['name', 'departments', 'company']
