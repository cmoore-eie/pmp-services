from ..models.model.ExternalProduct import ExternalProduct
from ..serializers.ExternalProductSerializer import ExternalProductSerializer
from rest_framework import viewsets


class ExternalProductViewSet(viewsets.ModelViewSet):
    queryset = ExternalProduct.objects.all()
    serializer_class = ExternalProductSerializer
