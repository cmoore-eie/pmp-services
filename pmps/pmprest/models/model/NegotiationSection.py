from django.db import models
from ..abstract.ItemLinkDelegate import ItemLinkDelegate


class NegotiationSection(ItemLinkDelegate):
    negotiation = models.ForeignKey('Negotiation', on_delete=models.CASCADE, related_name='negotiationSections', null=True)
    negotiationXML = models.TextField(null=True)
    name = models.CharField(max_length=255, blank=True)
    objects = models.Manager()

    def __str__(self):
        return f'{self.name}'
