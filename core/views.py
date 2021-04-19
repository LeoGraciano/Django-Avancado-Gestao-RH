from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .tasks import send_report


# Create your views here.


@login_required
def home(request):
    data = {'user': request.user}
    return render(request, 'core/index.html', data)


@login_required
def celery(request):
    send_report.delay()
    # messages.success(request, 'Foi')
    return HttpResponse('Tarefa adcionada na Fila')
