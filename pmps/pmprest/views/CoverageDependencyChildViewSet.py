from ..models.model.CoverageDependencyChild import CoverageDependencyChild
from ..serializers.CoverageDependencyChildSerializer import CoverageDependencyChildSerializer
from rest_framework import viewsets


class CoverageDependencyChildViewSet(viewsets.ModelViewSet):
    queryset = CoverageDependencyChild.objects.all()
    serializer_class = CoverageDependencyChildSerializer
