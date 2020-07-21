from drf_writable_nested import UniqueFieldsMixin
from rest_framework import serializers
from rest_framework.fields import BooleanField

from ..models.model.VirtualProductFlavour import VirtualProductFlavour


class VirtualProductFlavourSerializer(UniqueFieldsMixin, serializers.ModelSerializer):

    defaultFlavour = BooleanField()

    class Meta:
        model = VirtualProductFlavour
        fields = ['effectiveDate',
                  'expirationDate',
                  'itemIdentifier',
                  'ancestorItemIdentifier',
                  'defaultFlavour',
                  'name',
                  'code',
                  'lineCode',
                  'condition',
                  'priority',
                  'rank',
                  'grandfathering',
                  'defaultFlavour',
                  'purge', ]
