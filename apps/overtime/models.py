from core.models import BaseModelField
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Overtime(BaseModelField):
    reason = models.CharField('Motivo', max_length=100)
    employee = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='overtime', verbose_name='Funcionário')

    def __str__(self):
        return self.reason
