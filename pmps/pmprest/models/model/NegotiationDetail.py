from django.db import models
from ..abstract.ItemLinkDelegate import ItemLinkDelegate


class NegotiationDetail(ItemLinkDelegate):
    negotiationSection = models.ForeignKey('NegotiationSection', on_delete=models.CASCADE, related_name='negotiationDetails', null=True)
    negotiationXML = models.TextField(null=True)
    objects = models.Manager()

    def __str__(self):
        return f'{self.itemIdentifier}'
