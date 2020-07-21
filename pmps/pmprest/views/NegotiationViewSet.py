from ..models.model.Negotiation import Negotiation
from ..serializers.NegotiationSerializer import NegotiationSerializer
from rest_framework import viewsets


class NegotiationViewSet(viewsets.ModelViewSet):
    queryset = Negotiation.objects.all()
    serializer_class = NegotiationSerializer
