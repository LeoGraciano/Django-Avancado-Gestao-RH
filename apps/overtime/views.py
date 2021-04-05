from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.base import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import OverTime
from .forms import OverTimeForm
from apps.employees.models import Employee

# Create your views here.


class OverTimeListView(ListView):
    model = OverTime

    def get_queryset(self):
        company = self.request.user.employee.company
        return OverTime.objects.filter(employee__company=company)


class OverTimeUpdateView(UpdateView):
    model = OverTime
    form_class = OverTimeForm
    success_url = reverse_lazy('overtime:list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if hasattr(self, 'object'):
            kwargs.update({'instance': self.object})
            kwargs.update({'employee': self.request.user.employee})

        return kwargs


class OverTimeEmployeeUpdateView(UpdateView):
    model = OverTime
    form_class = OverTimeForm
    # success_url = reverse_lazy('overtime:list')

    def get_success_url(self):
        return reverse_lazy('employees:update', args=[self.object.employee.pk])

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if hasattr(self, 'object'):
            kwargs.update({'instance': self.object})
            kwargs.update({'employee': self.request.user.employee})

        return kwargs


class OverTimeDeleteView(DeleteView):
    model = OverTime
    success_url = reverse_lazy('overtime:list')


class OverTimeCreateView(CreateView):
    model = OverTime
    form_class = OverTimeForm
    success_url = reverse_lazy('overtime:list')

    # copiado de dentro do CreateView/ModelFormMixin e fazer um Overwrite(Sobre Escrita)
    def get_form_kwargs(self):
        """Return the keyword arguments for instantiating the form."""
        kwargs = super().get_form_kwargs()
        if hasattr(self, 'object'):
            kwargs.update({'instance': self.object})
            kwargs.update({'employee': self.request.user.employee})
        return kwargs


class UserOverTimeView(View):
    def post(self, *args, **kwargs):
        register_overtime = OverTime.objects.get(pk=kwargs['pk'])
        params = self.request.POST['params_recovery']
        if params == 'up':
            register_overtime.is_hours = True
        else:
            register_overtime.is_hours = False
        register_overtime.save(update_fields=['is_hours'])
        employee = register_overtime.employee
        response = {
            'message': 'Requisição executada com sucesso',
            'bank_hours': f'Saldo atual de {employee.overtime_total} horas restante agora',

        }

        return JsonResponse(response)
