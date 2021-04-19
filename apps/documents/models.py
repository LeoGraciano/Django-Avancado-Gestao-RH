from django.db import models
from django.contrib.auth.models import User
from core.models import BaseModelField
from django.urls.base import reverse_lazy
from django.shortcuts import redirect
from apps.employees.models import *
# Create your models here.


class Document(BaseModelField):
    description = models.CharField('Descriação', max_length=100)
    owner = models.ForeignKey(
        Employee, on_delete=models.PROTECT, verbose_name='Proprietário')
    file = models.FileField('Arquivo', blank=True,
                            null=True, upload_to='documents')

    def get_absolute_url(self):
        return reverse_lazy('employees:update', args=[self.owner.pk])

    def __str__(self):
        return self.description

    # class Meta:
    #     app_label = 'documents'
