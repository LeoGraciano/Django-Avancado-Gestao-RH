from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import OverTime
# Create your views here.


class OverTimeListView(ListView):
    model = OverTime

    def get_queryset(self):
        company = self.request.user.employee.company
        return OverTime.objects.filter(employee__company=company)
