from django.db import models
from ..abstract.ItemLinkDelegate import ItemLinkDelegate
from ..abstract.SchemeValueDelegate import SchemeValueDelegate


class SchemeDetailParam(ItemLinkDelegate, SchemeValueDelegate):
    schemeDetail = models.ForeignKey("SchemeDetail", on_delete=models.CASCADE, related_name="schemeDetailParams", null=True)
    schemeConditionParam = models.ForeignKey("SchemeConditionParam", on_delete=models.SET_NULL, null=True)
    objects = models.Manager()
