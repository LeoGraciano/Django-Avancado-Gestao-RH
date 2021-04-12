
from rest_framework import serializers
from apps.employees.models import Employee
from apps.overtime.api.serializers import OverTimeSerializer


# Serializers define the API representation.
class EmployeeSerializer(serializers.ModelSerializer):
    overtime_set = OverTimeSerializer(many=True)

    class Meta:
        model = Employee
        fields = ['name', 'departments', 'company', 'overtime_total',
                  'overtime_set']
