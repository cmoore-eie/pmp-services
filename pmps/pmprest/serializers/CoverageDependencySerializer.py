from rest_framework import serializers

from .CoverageDependencyChildSerializer import CoverageDependencyChildSerializer
from .CoverageDependencyParentSerializer import CoverageDependencyParentSerializer
from .CoverageDependencySelectSerializer import CoverageDependencySelectSerializer
from ..models.model.CoverageDependency import CoverageDependency


class CoverageDependencySerializer(serializers.ModelSerializer):
    coverageChildren = CoverageDependencyChildSerializer(many=True)
    coverageParents = CoverageDependencyParentSerializer(many=True)
    coverageSelection = CoverageDependencySelectSerializer(many=True)

    class Meta:
        model = CoverageDependency
        fields = ['effectiveDate',
                  'expirationDate',
                  'code',
                  'locked',
                  'jsonString',
                  'itemIdentifier',
                  'ancestorItemIdentifier',
                  'versionNumber',
                  'itemStatus',
                  'name',
                  'coverable',
                  'productCode',
                  'coverageChildren',
                  'coverageParents',
                  'coverageSelection', ]


