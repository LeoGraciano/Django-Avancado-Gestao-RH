from django.db import models
from django.contrib.auth.models import User
from core.models import BaseModelField
# Create your models here.


class Documents(BaseModelField):
    description = models.CharField('Descriação', max_length=100)
    owner = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name='Proprietário')

    def __str__(self):
        return self.description
