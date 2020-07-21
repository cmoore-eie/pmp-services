from django.db import models
from ..abstract.ItemLinkDelegate import ItemLinkDelegate
from ..abstract.PurgeableDelegate import PurgeableDelegate


class ContractAttachment(ItemLinkDelegate, PurgeableDelegate):
    contractVersion = models.ForeignKey('ContractVersion', on_delete=models.CASCADE, related_name='contractAttachments', null=True, blank=True)
    coverableCode = models.CharField(max_length=255, blank=True)
    coverableIncluded = models.BooleanField(default=True)
    objects = models.Manager()

    def __str__(self):
        return f'{self.itemIdentifier}'
