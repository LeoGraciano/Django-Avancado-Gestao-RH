

from django.contrib.auth.models import User, Group
from .serializers import GroupSerializer, UserSerializer
from rest_framework import viewsets


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
