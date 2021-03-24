from django.urls.base import reverse_lazy
from django.utils import timezone
from django.urls import reverse
from django.http.response import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Document
# Create your views here.


class EmployeeListView(ListView):
    model = Employee
    paginate_by = 5

    # get_queryset edita os items que vem do model Employee.objects.all()
    def get_queryset(self):
        company = self.request.user.employee.company
        queryset = Employee.objects.filter(company=company)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class EmployeeCreateView(CreateView):
    model = Employee
    fields = ['name', 'departments']
    success_url = reverse_lazy('employees:list')

    def form_valid(self, form):
        employee = form.save(commit=False)
        employee.company = self.request.user.employee.company
        username = f"{employee.name.split(' ')[0]}#{random_digits()}"
        employee.user = User.objects.create(username=username)
        employee.save()
        return super(EmployeeCreateView, self).form_valid(form)


class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = '__all__'
    success_url = reverse_lazy('employees:list')


class EmployeeDeleteView(DeleteView):
    model = Employee
    success_url = reverse_lazy('employees:list')
