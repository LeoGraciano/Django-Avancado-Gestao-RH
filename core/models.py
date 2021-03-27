from django.db import models
from uuid import uuid4

from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class BaseModelField(models.Model):
    code = models.UUIDField(
        primary_key=True, default=uuid4,
        editable=False,
        db_column='code_parameter'
    )

    """Classe de composição para modelos que utilizaram os
        campos created_at, updated_at
    """
    created_at = models.DateTimeField(
        _('Criado em'), auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        _('Aualizado em'), auto_now=True,

    )

    class Meta:
        abstract = True
