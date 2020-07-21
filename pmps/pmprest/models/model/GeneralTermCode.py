from django.db import models
from ..abstract.ItemLinkDelegate import ItemLinkDelegate
from ..dictionary.Channel import Channel


class GeneralTermCode(ItemLinkDelegate):
    generalTerm = models.ForeignKey('GeneralTerm', on_delete=models.CASCADE, related_name='generalTermCodes', null=True)
    code = models.CharField(max_length=255, blank=True)
    externalReference = models.CharField(max_length=255, blank=True)
    processOrder = models.IntegerField(null=True)
    objects = models.Manager()

    Channel = models.CharField(
        max_length=30,
        choices=Channel.choices,
        default=Channel.callcenter
    )

    def __str__(self):
        return f'{self.code} - {self.itemIdentifier}'
