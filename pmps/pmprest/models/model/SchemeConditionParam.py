from django.db import models
from ..abstract.ItemLinkDelegate import ItemLinkDelegate
from ..dictionary.AttributeValueType import AttributeValueType


class SchemeConditionParam(ItemLinkDelegate):
    schemeCondition = models.ForeignKey("SchemeCondition", on_delete=models.CASCADE, related_name="schemeConditionParams", null=True)
    parameter = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255, blank=True)
    objects = models.Manager()

    paramValueType = models.CharField(
        max_length=30,
        choices=AttributeValueType.choices,
        default=AttributeValueType.stringType
    )

    def __str__(self):
        return f'{self.name}'
