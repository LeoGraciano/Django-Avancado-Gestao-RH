from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=100, help_text='Nome da Company')

    def __str__(self):
        return self.name
