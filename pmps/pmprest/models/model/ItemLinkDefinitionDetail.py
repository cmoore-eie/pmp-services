from django.db import models
from ..dictionary.AttributeValueType import AttributeValueType


class ItemLinkDefinitionDetail(models.Model):
    itemLinkDefinition = models.ForeignKey('ItemLinkDefinition', on_delete=models.CASCADE, related_name='ItemLinkDefinitionDetails')
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255, blank=True)
    value = models.CharField(max_length=255, blank=True)
    objects = models.Manager()

    valueType = models.CharField(
        max_length=30,
        choices=AttributeValueType.choices,
        default=AttributeValueType.stringType
    )

    def __str__(self):
        return f'{self.code} - {self.name}'
