from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from apps.employees.models import Employee
from django.contrib.auth.models import User
from .api.serializers import GroupSerializer, UserSerializer
from rest_framework import viewsets

# Create your views here.


@login_required
def home(request):
    data = {'user': request.user}
    return render(request, 'core/index.html', data)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
