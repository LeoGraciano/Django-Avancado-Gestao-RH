from core.models import BaseModelField
from django.db import models
from django.contrib.auth.models import User
from apps.employees.models import *

# Create your models here.


class OverTime(BaseModelField):
    reason = models.CharField('Motivo', max_length=100)
    employee = models.ForeignKey(
        Employee, on_delete=models.PROTECT, verbose_name='Funcionário')
    hours = models.DecimalField(max_digits=5, decimal_places=2)
    is_hours = models.BooleanField(default=True, editable=False)

    def __str__(self):
        return self.reason

    # class Meta:
    #     app_label = 'overtime'
