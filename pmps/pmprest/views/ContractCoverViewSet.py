from ..models.model.ContractCover import ContractCover
from ..serializers.ContractCoverSerializer import ContractCoverSerializer
from rest_framework import viewsets


class ContractCoverViewSet(viewsets.ModelViewSet):
    queryset = ContractCover.objects.all()
    serializer_class = ContractCoverSerializer
