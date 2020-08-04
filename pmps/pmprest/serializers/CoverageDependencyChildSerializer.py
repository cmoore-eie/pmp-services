from rest_framework import serializers
from ..models.model.CoverageDependencyChild import CoverageDependencyChild


class CoverageDependencyChildSerializer(serializers.ModelSerializer):

    class Meta:
        model = CoverageDependencyChild
        fields = ['itemIdentifier',
                  'ancestorItemIdentifier',
                  'coverageCode',
                  'coverageDependency', ]

