from ..models.model.CoverageDependencyParent import CoverageDependencyParent
from ..serializers.CoverageDependencyParentSerializer import CoverageDependencyParentSerializer
from rest_framework import viewsets


class CoverageDependencyParentViewSet(viewsets.ModelViewSet):
    queryset = CoverageDependencyParent.objects.all()
    serializer_class = CoverageDependencyParentSerializer
