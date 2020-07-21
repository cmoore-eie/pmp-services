from django.db import models
from ..abstract.EffectiveExpirationDate import EffectiveExpirationDate
from ..abstract.ItemStatusDelegate import ItemStatusDelegate
from ..abstract.ItemLinkDelegate import ItemLinkDelegate
from ..abstract.ItemDelegate import ItemDelegate
from ..dictionary.SchemeCreateMethod import SchemeCreateMethod
from ..dictionary.SchemeType import SchemeType


class Scheme(ItemStatusDelegate, ItemDelegate, ItemLinkDelegate, EffectiveExpirationDate):
    name = models.CharField(max_length=255, blank=True)
    productCode = models.CharField(max_length=255, blank=True)
    renewalAvailable = models.BooleanField(default=True)
    autoImportDate = models.DateTimeField(null=True)
    description = models.TextField(null=True)
    private = models.BooleanField(default=False)
    objects = models.Manager()

    schemeType = models.CharField(
        max_length=30,
        choices=SchemeType.choices,
        default=SchemeType.PUBLIC_SCHEME
    )

    createMethod = models.CharField(
        max_length=30,
        choices=SchemeCreateMethod.choices,
        default=SchemeCreateMethod.MANUAL
    )

    def __str__(self):
        return f'{self.code} - {self.name}'
