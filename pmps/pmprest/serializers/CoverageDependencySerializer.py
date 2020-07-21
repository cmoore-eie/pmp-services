from rest_framework import serializers

from .CoverageDependencyChildSerializer import CoverageDependencyChildSerializer
from .CoverageDependencyParentSerializer import CoverageDependencyParentSerializer
from ..models.model.CoverageDependency import CoverageDependency


class CoverageDependencySerializer(serializers.ModelSerializer):
    coverageChildren = CoverageDependencyChildSerializer(many=True)
    coverageParents = CoverageDependencyParentSerializer(many=True)
    coverageSelection = CoverageDependencyParentSerializer(many=True)

    class Meta:
        model = CoverageDependency
        fields = '__all__'

