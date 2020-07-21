from ..filters.VirtualProductFilterSet import VirtualProductFilterSet
from ..models.model.VirtualProduct import VirtualProduct
from ..serializers.VirtualProductSerializer import VirtualProductSerializer
from rest_framework import viewsets


class VirtualProductViewSet(viewsets.ModelViewSet):
    queryset = VirtualProduct.objects.all()
    serializer_class = VirtualProductSerializer
    filterset_class = VirtualProductFilterSet
