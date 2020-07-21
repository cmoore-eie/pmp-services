from ..models.model.NegotiationDetail import NegotiationDetail
from ..serializers.NegotiationDetailSerializer import NegotiationDetailSerializer
from rest_framework import viewsets


class NegotiationDetailViewSet(viewsets.ModelViewSet):
    queryset = NegotiationDetail.objects.all()
    serializer_class = NegotiationDetailSerializer
