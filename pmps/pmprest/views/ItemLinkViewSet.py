from ..models.model.ItemLink import ItemLink
from ..serializers.ItemLinkSerializer import ItemLinkSerializer
from rest_framework import viewsets


class ItemLinkViewSet(viewsets.ModelViewSet):
    queryset = ItemLink.objects.all()
    serializer_class = ItemLinkSerializer
