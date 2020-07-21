from django.db import models
from ..dictionary.ConditionLogicOper import ConditionLogicOper
from ..abstract.ItemLinkDelegate import ItemLinkDelegate


class CoverageDependencyParent(ItemLinkDelegate):
    coverageDependency = models.ForeignKey("CoverageDependency", on_delete=models.CASCADE, related_name="coverageParents", null=True)
    coverageCode = models.CharField(max_length=255, blank=True)
    leftParenthesis = models.CharField(max_length=255, blank=True)
    rightParenthesis = models.CharField(max_length=255, blank=True)
    itemSequence = models.IntegerField(default=10)
    objects = models.Manager()

    conditionLogic = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        choices=ConditionLogicOper.choices
    )

    def __str__(self):
        return f'{self.itemIdentifier}'
