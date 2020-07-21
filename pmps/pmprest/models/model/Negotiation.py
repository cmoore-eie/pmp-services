from django.db import models
from ..abstract.EffectiveExpirationDate import EffectiveExpirationDate
from ..abstract.ItemStatusDelegate import ItemStatusDelegate
from ..abstract.ItemLinkDelegate import ItemLinkDelegate
from ..abstract.ItemDelegate import ItemDelegate
from ..dictionary.NegotiationStatus import NegotiationStatus


class Negotiation(EffectiveExpirationDate, ItemStatusDelegate, ItemDelegate, ItemLinkDelegate):
    individualPolicies = models.BooleanField()
    active = models.BooleanField()
    productCode = models.CharField(max_length=255, blank=True)
    objects = models.Manager()

    negotiationStatus = models.CharField(
        max_length=30,
        choices=NegotiationStatus.choices,
        default=NegotiationStatus.inprogress
    )

    def __str__(self):
        return f'{self.code} - {self.itemIdentifier}'
