from django.db import models
from ..abstract.ItemLinkDelegate import ItemLinkDelegate
from ..abstract.SchemeValueDelegate import SchemeValueDelegate
from ..dictionary.SchemeSourceType import SchemeSourceType
from ..dictionary.AttributeValueType import AttributeValueType
from ..dictionary.SchemeValidationType import SchemeValidationType
from ..dictionary.SchemeOperatorType import SchemeOperatorType
from ..dictionary.Currency import Currency
from ..dictionary.SchemeCostType import SchemeCostType
from ..dictionary.SchemeTimeframe import SchemeTimeframe


class SchemeDetail(ItemLinkDelegate, SchemeValueDelegate):
    scheme = models.ForeignKey("Scheme", on_delete=models.CASCADE, related_name="schemeDetails", null=True, blank=True)
    comparator = models.CharField(max_length=255, blank=True)
    parentCode = models.CharField(max_length=255, blank=True)
    condition = models.TextField(null=True)
    forceValue = models.BooleanField(default=True)
    timeDuration = models.IntegerField(null=True)
    costDiscount = models.FloatField(null=True)
    minMax = models.CharField(max_length=255, blank=True)
    objects = models.Manager()

    currency = models.CharField(
        max_length=30,
        choices=Currency.choices,
        blank=True,
        null=True
    )

    schemeCostType = models.CharField(
        max_length=30,
        choices=SchemeCostType.choices,
        blank=True,
        null=True
    )

    schemeOperatorType = models.CharField(
        max_length=30,
        choices=SchemeOperatorType.choices,
        blank=True,
        null = True
    )

    schemeSourceType = models.CharField(
        max_length=30,
        choices=SchemeSourceType.choices
    )

    schemeTimeframe = models.CharField(
        max_length=30,
        choices=SchemeTimeframe.choices,
        blank=True,
        null=True
    )

    schemeValueType = models.CharField(
        max_length=30,
        choices=AttributeValueType.choices,
        blank=True,
        null=True
    )

    schemeValidationType = models.CharField(
        max_length=30,
        choices=SchemeValidationType.choices,
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.itemIdentifier}'
