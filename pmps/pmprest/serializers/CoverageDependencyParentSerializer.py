from rest_framework import serializers
from ..models.model.CoverageDependencyParent import CoverageDependencyParent


class CoverageDependencyParentSerializer(serializers.ModelSerializer):

    class Meta:
        model = CoverageDependencyParent
        fields = '__all__'

