from django.db import models
from core.models import BaseModelField
from django.views.generic.edit import CreateView
# Create your models here.


class Company(BaseModelField):
    name = models.CharField(max_length=100, help_text='Nome da Company')

    def __str__(self):
        return self.name
