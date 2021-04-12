from rest_framework import viewsets
from apps.overtime.models import OverTime
from .serializers import OverTimeSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# API
class OverTimeViewSet(viewsets.ModelViewSet):
    queryset = OverTime.objects.all()
    serializer_class = OverTimeSerializer
    # authentication e permissions Manual
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
