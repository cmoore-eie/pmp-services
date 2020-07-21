from ..filters.ContractFilterSet import ContractFilterSet
from ..models.model.Contract import Contract
from ..serializers.ContractSerializer import ContractSerializer
from rest_framework import viewsets


class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    filterset_class = ContractFilterSet
