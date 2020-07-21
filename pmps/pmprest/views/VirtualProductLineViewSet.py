from ..models.model.VirtualProductLine import VirtualProductLine
from ..serializers.VirtualProductLineSerializer import VirtualProductLineSerializer
from rest_framework import viewsets


class VirtualProductLineViewSet(viewsets.ModelViewSet):
    queryset = VirtualProductLine.objects.all()
    serializer_class = VirtualProductLineSerializer
