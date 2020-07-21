from django.db import models
from ..abstract.ItemLinkDelegate import ItemLinkDelegate
from ..abstract.SchemeValueDelegate import SchemeValueDelegate


class SchemeDetailArrayValue(ItemLinkDelegate, SchemeValueDelegate):
    schemeDetail = models.ForeignKey("SchemeDetail", on_delete=models.CASCADE, related_name="schemeDetailArrayValues", null=True)
    comparator = models.CharField(max_length=255, blank=True)
    parentCode = models.CharField(max_length=255, blank=True)
    objects = models.Manager()

    def __str__(self):
        return f'{self.itemIdentifier}'
