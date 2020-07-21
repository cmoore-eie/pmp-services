from django.db import models
from ..abstract.ItemLinkDelegate import ItemLinkDelegate


class ConditionLogicDetail(ItemLinkDelegate):
    conditionLogic = models.ForeignKey('ConditionLogic', on_delete=models.CASCADE, related_name='conditionLogicDetails', null=True)
    objects = models.Manager()

    def __str__(self):
        return f'{self.itemIdentifier}'
