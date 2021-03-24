from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Department
from django.urls.base import reverse_lazy
from django.contrib.auth.models import User
# Create your views here.


class DepartmentListView(ListView):
    model = Department

    def get_queryset(self):
        company = self.request.user.employee.company
        return Department.objects.filter(company=company)


class DepartmentCreateView(CreateView):
    model = Department
    fields = ['name']
    success_url = reverse_lazy('departments:list')

    def form_valid(self, form):
        department = form.save(commit=False)
        # ManytoMany você salva primeiro o objeto depois pode add no field.
        department.save()
        company = self.request.user.employee.company
        department.company.add(company)
        return super(DepartmentCreateView, self).form_valid(form)


class DepartmentUpdateView(UpdateView):
    model = Department
    fields = ['name']
    success_url = reverse_lazy('departments:list')


class DepartmentDeleteView(DeleteView):
    model = Department
    success_url = reverse_lazy('departments:list')
