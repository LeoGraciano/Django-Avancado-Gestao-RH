from django.urls.base import reverse_lazy
from django.utils import timezone
from django.urls import reverse
from django.http.response import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Document
from apps.employees.models import Employee
# Create your views here.


class DocumentListView(ListView):
    model = Document


class DocumentCreateView(CreateView):
    model = Document
    fields = ['description', 'file']

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        employee = Employee.objects.get(pk=self.kwargs['pk'])
        form.instance.owner = employee

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class DocumentUpdateView(UpdateView):
    model = Document
    fields = '__all__'
    success_url = reverse_lazy('employees:list')


class DocumentDeleteView(DeleteView):
    model = Document
    success_url = reverse_lazy('employees:list')
