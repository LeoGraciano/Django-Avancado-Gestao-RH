
from rest_framework import serializers
from apps.overtime.models import OverTime


# Serializers define the API representation.
class OverTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OverTime
        fields = ['reason', 'employee', 'hours', 'is_hours']
