from django.db import models
from ..abstract.ItemLinkDelegate import ItemLinkDelegate


class CoverageDependencyChild(ItemLinkDelegate):
    coverageDependency = models.ForeignKey('CoverageDependency', on_delete=models.CASCADE, related_name='coverageChildren', null=True)
    coverageCode = models.CharField(max_length=255, blank=True)
    objects = models.Manager()

    def __str__(self):
        return f'{self.itemIdentifier}'
