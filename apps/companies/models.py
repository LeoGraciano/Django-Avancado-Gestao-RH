from django.db import models
from core.models import BaseModelField
# Create your models here.


class Company(BaseModelField):
    name = models.CharField('Nome', max_length=100)

    def __str__(self):
        return self.name
