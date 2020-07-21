from django.db import models
from ..abstract.ItemDelegate import ItemDelegate
from ..abstract.ItemLinkDelegate import ItemLinkDelegate
from ..abstract.ItemStatusDelegate import ItemStatusDelegate


class Contract(ItemDelegate, ItemLinkDelegate, ItemStatusDelegate):
    name = models.CharField(max_length=255, blank=True)
    productCode = models.CharField(max_length=255, blank=True)
    objects = models.Manager()

    def __str__(self):
        return f'{self.code} - {self.name}'
