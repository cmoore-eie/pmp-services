from django.db import models
from ..abstract.EffectiveExpirationDate import EffectiveExpirationDate
from ..abstract.ItemStatusDelegate import ItemStatusDelegate
from ..abstract.ItemDelegate import ItemDelegate
from ..abstract.ItemLinkDelegate import ItemLinkDelegate
from ..dictionary.VirtualProductType import VirtualProductType


class VirtualProduct(EffectiveExpirationDate, ItemStatusDelegate, ItemDelegate, ItemLinkDelegate):
    name = models.CharField(max_length=255, blank=True)
    productCode = models.CharField(max_length=255, blank=True)
    allowAffinity = models.BooleanField(default=False)
    allowCampaign = models.BooleanField(default=False)
    objects = models.Manager()

    VirtualProductType = models.CharField(
        max_length=30,
        choices=VirtualProductType.choices,
        default=VirtualProductType.OPEN_VP
    )
