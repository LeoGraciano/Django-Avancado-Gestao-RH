from django.db import models
from core.models import BaseModelField

# Create your models here.


class Department(BaseModelField):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name
