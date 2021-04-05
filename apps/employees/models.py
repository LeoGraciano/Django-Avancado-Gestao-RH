from django.db import models
from django.db.models.aggregates import Sum
from core.models import BaseModelField
from django.contrib.auth.models import User
from apps.departments.models import Department
from apps.companies.models import Company
from django.shortcuts import redirect
from django.urls import reverse
# Create your models here.


class Employee(BaseModelField):

    name = models.CharField('Nome', max_length=100)
    user = models.OneToOneField(
        User, on_delete=models.PROTECT, verbose_name='Usuário')

    departments = models.ManyToManyField(
        Department, verbose_name='Departamentos')

    company = models.ForeignKey(
        Company, on_delete=models.PROTECT, blank=True, null=True, verbose_name='Empresas')

    def __str__(self):
        return self.name

    @property
    def overtime_total(self):
        total = self.overtime_set.exclude(
            is_hours=False).aggregate(Sum('hours'))['hours__sum']

        return total or 0

    class meta:
        ordering = 'name'
