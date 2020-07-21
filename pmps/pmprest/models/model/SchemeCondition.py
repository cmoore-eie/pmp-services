from django.db import models
from ..abstract.EffectiveExpirationDate import EffectiveExpirationDate
from ..abstract.ItemStatusDelegate import ItemStatusDelegate
from ..abstract.ItemDelegate import ItemDelegate
from ..abstract.ItemLinkDelegate import ItemLinkDelegate


class SchemeCondition(EffectiveExpirationDate, ItemStatusDelegate, ItemDelegate, ItemLinkDelegate):
    name = models.CharField(max_length=225, blank=True)
    condition = models.CharField(max_length=500, blank=True)
    producerCode = models.CharField(max_length=255, blank=True)
    root = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=500, blank=True)
    objects = models.Manager()

    def __str__(self):
        return f'{self.code} - {self.name}'
