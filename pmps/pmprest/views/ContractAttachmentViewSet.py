from ..models.model.ContractAttachment import ContractAttachment
from ..serializers.ContractAttachmentSerializer import ContractAttachmentSerializer
from rest_framework import viewsets


class ContractAttachmentViewSet(viewsets.ModelViewSet):
    queryset = ContractAttachment.objects.all()
    serializer_class = ContractAttachmentSerializer
