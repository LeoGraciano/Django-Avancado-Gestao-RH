from django.db import models

from django.shortcuts import redirect
from core.models import BaseModelField
# Create your models here.


class Company(BaseModelField):
    name = models.CharField('Nome', max_length=100)

    def __str__(self):
        return self.name

    # class Meta:
    #     app_label = 'companies'
