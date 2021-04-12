from rest_framework import viewsets
from apps.overtime.models import OverTime
from .serializers import OverTimeSerializer


# API
class OverTimeViewSet(viewsets.ModelViewSet):
    queryset = OverTime.objects.all()
    serializer_class = OverTimeSerializer
