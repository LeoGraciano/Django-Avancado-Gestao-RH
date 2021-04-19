from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from apps.employees.models import Employee


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def count_widgets():
    return Widget.objects.count()


@shared_task
def rename_widget(widget_id, name):
    w = Widget.objects.get(id=widget_id)
    w.name = name
    w.save()


@shared_task
def send_report():
    e_counts = Employee.objects.count()
    send_mail(
        _('Relatorio Celery'),
        _(f'Quantidade de Funcionários {e_counts}'),
        'suporteban@gmail.com',
        ['contato@suporteban.com'],
        fail_silently=False
    )
    return True
