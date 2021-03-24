from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from apps.employees.models import Employee
# Create your views here.


@login_required
def home(request):
    data = {'user': request.user}
    return render(request, 'core/index.html', data)
