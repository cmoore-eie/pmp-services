from django.db import models
from ..abstract.EffectiveExpirationDate import EffectiveExpirationDate
from ..abstract.ItemLinkDelegate import ItemLinkDelegate
from ..abstract.PurgeableDelegate import PurgeableDelegate
from ..dictionary.VirtualFlavourAction import VirtualFlavourAction


class VirtualProductFlavour(EffectiveExpirationDate, ItemLinkDelegate, PurgeableDelegate):
    virtualProduct = models.ForeignKey("VirtualProduct", on_delete=models.CASCADE, related_name="virtualProductFlavours", null=True, blank=True)
    defaultFlavour = models.BooleanField(default=False)
    name = models.CharField(max_length=255, blank=True)
    code = models.CharField(max_length=255, blank=True)
    lineCode = models.CharField(max_length=255, blank=True)
    condition = models.TextField(null=True, blank=True)
    priority = models.IntegerField(null=True)
    rank = models.IntegerField(null=True)
    objects = models.Manager()

    grandfathering = models.CharField(
        max_length=30,
        choices=VirtualFlavourAction.choices,
        null=True,
        blank=True,
    )
