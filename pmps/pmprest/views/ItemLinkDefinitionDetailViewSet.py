from ..models.model.ItemLinkDefinitionDetail import ItemLinkDefinitionDetail
from ..serializers.ItemLinkDefinitionDetailSerializer import ItemLinkDefinitionDetailSerializer
from rest_framework import viewsets


class ItemLinkDefinitionDetailViewSet(viewsets.ModelViewSet):
    queryset = ItemLinkDefinitionDetail.objects.all()
    serializer_class = ItemLinkDefinitionDetailSerializer
