from django.db import models
from django.contrib.auth.models import User
from apps.departments.models import Department
from apps.companies.models import Company
# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=100)
    employee = models.OneToOneField(
        User, on_delete=models.PROTECT, verbose_name='Funcionário')

    departments = models.ManyToManyField(
        Department)

    companies = models.ForeignKey(
        Company, on_delete=models.PROTECT, blank=True, null=True, verbose_name='Empresas')

    def __str__(self):
        return self.name
