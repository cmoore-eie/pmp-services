from django.db import models
from ..abstract.ItemStatusDelegate import ItemStatusDelegate
from ..abstract.EffectiveExpirationDate import EffectiveExpirationDate
from ..abstract.ItemDelegate import ItemDelegate
from ..abstract.ItemLinkDelegate import ItemLinkDelegate


class ConditionLogic(ItemStatusDelegate, EffectiveExpirationDate, ItemDelegate, ItemLinkDelegate):
    logicCode = models.CharField(max_length=500, blank=True)
    name = models.CharField(max_length=255, blank=True)
    productCode = models.CharField(max_length=255, blank=True)
    objects = models.Manager()

    def __str__(self):
        return f'{self.code} - {self.name}'
