from django.db import models
from core.models import BaseModelField
from apps.companies.models import Company
# Create your models here.


class Department(BaseModelField):
    name = models.CharField('Nome', max_length=70)
    company = models.ManyToManyField(
        Company, verbose_name='Empresas')

    def __str__(self):
        return self.name

    # class Meta:
    #     app_label = 'departments'
