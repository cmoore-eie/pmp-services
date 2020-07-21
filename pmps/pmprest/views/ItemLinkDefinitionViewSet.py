from ..models.model.ItemLinkDefinition import ItemLinkDefinition
from ..serializers.ItemLinkDefinitionSerializer import ItemLinkDefinitionSerializer
from rest_framework import viewsets


class ItemLinkDefinitionViewSet(viewsets.ModelViewSet):
    queryset = ItemLinkDefinition.objects.all()
    serializer_class = ItemLinkDefinitionSerializer
