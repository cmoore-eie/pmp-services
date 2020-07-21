from django.db import models
from ..abstract.ItemLinkDelegate import ItemLinkDelegate
from ..abstract.PurgeableDelegate import PurgeableDelegate


class VirtualProductCategory(ItemLinkDelegate, PurgeableDelegate):
    virtualProduct = models.ForeignKey("VirtualProduct", on_delete=models.CASCADE, related_name="virtualProductCategories", null=True, blank=True)
    name = models.CharField(max_length=255, blank=True)
    code = models.CharField(max_length=255, blank=True)
    priority = models.IntegerField(null=True)
    objects = models.Manager()
