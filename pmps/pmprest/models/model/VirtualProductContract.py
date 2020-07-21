from django.db import models
from ..abstract.ItemLinkDelegate import ItemLinkDelegate
from ..abstract.PurgeableDelegate import PurgeableDelegate


class VirtualProductContract(ItemLinkDelegate, PurgeableDelegate):
    virtualProduct = models.ForeignKey("VirtualProduct", on_delete=models.CASCADE, related_name="virtualProductContracts", null=True)
    contract = models.ForeignKey("Contract", on_delete=models.SET_NULL, null=True)
    priority = models.IntegerField(null=True)
    contractIdentifier = models.CharField(max_length=255, blank=True, null=True)
    objects = models.Manager()
