from ..models.model.NegotiationSection import NegotiationSection
from ..serializers.NegotiationSectionSerializer import NegotiationSectionSerializer
from rest_framework import viewsets


class NegotiationSectionViewSet(viewsets.ModelViewSet):
    queryset = NegotiationSection.objects.all()
    serializer_class = NegotiationSectionSerializer
