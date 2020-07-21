from ..models.model.CoverageDependencySelect import CoverageDependencySelect
from ..serializers.CoverageDependencySelectSerializer import CoverageDependencySelectSerializer
from rest_framework import viewsets


class CoverageDependencySelectViewSet(viewsets.ModelViewSet):
    queryset = CoverageDependencySelect.objects.all()
    serializer_class = CoverageDependencySelectSerializer
