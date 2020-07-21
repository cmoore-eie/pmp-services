from django.db import models
from ..abstract.ItemStatusDelegate import ItemStatusDelegate
from ..abstract.ItemDelegate import ItemDelegate
from ..abstract.ItemLinkDelegate import ItemLinkDelegate
from ..abstract.EffectiveExpirationDate import EffectiveExpirationDate


class ExternalProduct(EffectiveExpirationDate, ItemStatusDelegate, ItemDelegate, ItemLinkDelegate):
    productCode = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255, blank=True)
    objects = models.Manager()

    def __str__(self):
        return f'{self.code} - {self.name}'
