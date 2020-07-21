from ..models.model.VirtualProductContract import VirtualProductContract
from ..serializers.VirtualProductContractSerializer import VirtualProductContractSerializer
from rest_framework import viewsets


class VirtualProductContractViewSet(viewsets.ModelViewSet):
    queryset = VirtualProductContract.objects.all()
    serializer_class = VirtualProductContractSerializer
