from rest_framework import serializers
from ..models.model.CoverageDependencySelect import CoverageDependencySelect


class CoverageDependencySelectSerializer(serializers.ModelSerializer):

    class Meta:
        model = CoverageDependencySelect
        fields = ['itemIdentifier',
                  'ancestorItemIdentifier',
                  'coverageCode',
                  'coverageDependency', ]

