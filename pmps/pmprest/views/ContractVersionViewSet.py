from ..models.model.ContractVersion import ContractVersion
from ..serializers.ContractVersionSerializer import ContractVersionSerializer
from rest_framework import viewsets


class ContractVersionViewSet(viewsets.ModelViewSet):
    queryset = ContractVersion.objects.all()
    serializer_class = ContractVersionSerializer
