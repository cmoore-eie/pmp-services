from django.db import models
from ..abstract.EffectiveExpirationDate import EffectiveExpirationDate
from ..abstract.ItemLinkDelegate import ItemLinkDelegate
from ..abstract.PurgeableDelegate import PurgeableDelegate
from ..dictionary.ExistenceType import ExistenceType


class ContractVersion(EffectiveExpirationDate, ItemLinkDelegate, PurgeableDelegate):
    contract = models.ForeignKey('Contract', on_delete=models.CASCADE, related_name='contractVersions', null=True, blank=True)
    versionNumber = models.IntegerField(default=1)
    hiddenContract = models.BooleanField(default=False)
    objects = models.Manager()

    existence = models.CharField(
        max_length=20,
        choices=ExistenceType.choices,
        default=ExistenceType.Suggested
    )

    def __str__(self):
        return f'{self.itemIdentifier}'
