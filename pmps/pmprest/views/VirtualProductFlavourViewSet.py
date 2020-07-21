from ..models.model.VirtualProductFlavour import VirtualProductFlavour
from ..serializers.VirtualProductFlavourSerializer import VirtualProductFlavourSerializer
from rest_framework import viewsets


class VirtualProductFlavourViewSet(viewsets.ModelViewSet):
    queryset = VirtualProductFlavour.objects.all()
    serializer_class = VirtualProductFlavourSerializer
