from ..models.model.ExternalAttributeValue import ExternalAttributeValue
from ..serializers.ExternalAttributeValueSerializer import ExternalAttributeValueSerializer
from rest_framework import viewsets


class ExternalAttributeValueViewSet(viewsets.ModelViewSet):
    queryset = ExternalAttributeValue.objects.all()
    serializer_class = ExternalAttributeValueSerializer
