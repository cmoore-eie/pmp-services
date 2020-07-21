from django.db import models
from ..dictionary.SchemeCalcValueType import SchemeCalcValueType


class SchemeValueDelegate(models.Model):
    stringValue = models.CharField(max_length=255, blank=True, null=True)
    booleanValue = models.BooleanField(null=True)
    dateValue = models.DateField(null=True)
    integerValue = models.IntegerField(null=True)
    decimalValue = models.DecimalField(max_digits=19, decimal_places=10, null=True)
    moneyValue = models.DecimalField(max_digits=19, decimal_places=10, null=True)

    schemeCalcValueType = models.CharField(
        max_length=20,
        choices=SchemeCalcValueType.choices,
        default=SchemeCalcValueType.TEST,
        null=True
    )

    class Meta:
        abstract = True
