from django.db import models
from ..abstract.ItemLinkDelegate import ItemLinkDelegate
from ..dictionary.AttributeValueType import AttributeValueType


class ExternalAttributeValue(ItemLinkDelegate):
    externalProduct = models.ForeignKey('ExternalProduct', on_delete=models.CASCADE, related_name='externalAttributeValues', null=True)
    attributeName = models.CharField(max_length=255, blank=True)
    attributeValue = models.CharField(max_length=255, blank=True)
    entityName = models.CharField(max_length=255, blank=True)
    displayValue = models.CharField(max_length=255, blank=True)
    priority = models.IntegerField(null=True)
    typelistName = models.CharField(max_length=255, blank=True)
    objects = models.Manager()

    valueType = models.CharField(
        max_length=30,
        choices=AttributeValueType.choices,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f'{self.itemIdentifier}'
