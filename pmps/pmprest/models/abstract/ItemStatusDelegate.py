from django.db import models
from ..dictionary import ItemStatus


class ItemStatusDelegate(models.Model):
    versionNumber = models.IntegerField(default=1)

    itemStatus = models.CharField(
        max_length=20,
        choices=ItemStatus.ItemStatus.choices,
        default=ItemStatus.ItemStatus.DRAFT
    )

    class Meta:
        abstract = True
