from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView
from .models import Company
# Create your views here.


class CompanyCreateView(CreateView):
    model = Company
    fields = '__all__'

    def form_valid(self, form):
        obj = form.save()
        employee = self.request.user.employee
        employee.company = obj
        employee.save()

    def get_success_url(self):
        return reverse('core:index')


class CompanyUpdateView(UpdateView):
    model = Company
    fields = '__all__'

    def get_success_url(self):
        return reverse('core:index')
