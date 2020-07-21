from django.db import models
from ..abstract.ItemDelegate import ItemDelegate
from ..abstract.ItemLinkDelegate import ItemLinkDelegate
from ..abstract.EffectiveExpirationDate import EffectiveExpirationDate
from ..abstract.ItemStatusDelegate import ItemStatusDelegate
from ..dictionary.GeneralTermAttachment import GeneralTermAttachment


class GeneralTerm(ItemDelegate, ItemLinkDelegate, EffectiveExpirationDate, ItemStatusDelegate):
    name = models.CharField(max_length=255, blank=True)
    productCode = models.CharField(max_length=255, blank=True)
    lineCode = models.CharField(max_length=255, blank=True)
    objects = models.Manager()

    GeneralTermAttachment = models.CharField(
        max_length=30,
        choices=GeneralTermAttachment.choices,
        default=GeneralTermAttachment.Policy
    )

    def __str__(self):
        return f'{self.code} - {self.name}'
