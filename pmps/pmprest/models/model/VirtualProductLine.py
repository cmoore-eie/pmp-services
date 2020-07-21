from django.db import models
from ..abstract.ItemLinkDelegate import ItemLinkDelegate
from ..abstract.PurgeableDelegate import PurgeableDelegate


class VirtualProductLine(ItemLinkDelegate, PurgeableDelegate):
    virtualProduct = models.ForeignKey("VirtualProduct", on_delete=models.CASCADE, related_name="virtualProductLines", null=True)
    lineCode = models.CharField(max_length=255, blank=True)
    lineAvailable = models.BooleanField()
    objects = models.Manager()
