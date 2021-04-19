from django.db import models
from core.models import BaseModelField

# Create your models here.


class Test(BaseModelField):
    description = models.TextField()

    def __str__(self):
        return self.description

    # class Meta:
    #     app_label = 'app_old'
