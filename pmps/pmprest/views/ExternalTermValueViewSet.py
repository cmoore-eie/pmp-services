from ..models.model.ExternalTermValue import ExternalTermValue
from ..serializers.ExternalTermValueSerializer import ExternalTermValueSerializer
from rest_framework import viewsets


class ExternalTermValueViewSet(viewsets.ModelViewSet):
    queryset = ExternalTermValue.objects.all()
    serializer_class = ExternalTermValueSerializer
