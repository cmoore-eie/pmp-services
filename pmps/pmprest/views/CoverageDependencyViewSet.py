from ..models.model.CoverageDependency import CoverageDependency
from ..serializers.CoverageDependencySerializer import CoverageDependencySerializer
from rest_framework import viewsets


class CoverageDependencyViewSet(viewsets.ModelViewSet):
    queryset = CoverageDependency.objects.all()
    serializer_class = CoverageDependencySerializer
