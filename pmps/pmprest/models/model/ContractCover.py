from django.db import models
from ..abstract.ItemLinkDelegate import ItemLinkDelegate
from ..abstract.PurgeableDelegate import PurgeableDelegate


class ContractCover(ItemLinkDelegate, PurgeableDelegate):
    contractVersion = models.ForeignKey('ContractVersion', on_delete=models.CASCADE, related_name='contractCovers', null=True, blank=True)
    coverageCode = models.CharField(max_length=255, blank=True)
    coverIncluded = models.BooleanField(default=True)
    objects = models.Manager()

    def __str__(self):
        return f'{self.itemIdentifier}'
