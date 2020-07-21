from ..models.model.ItemLinkDetail import ItemLinkDetail
from ..serializers.ItemLinkDetailSerializer import ItemLinkDetailSerializer
from rest_framework import viewsets


class ItemLinkDetailViewSet(viewsets.ModelViewSet):
    queryset = ItemLinkDetail.objects.all()
    serializer_class = ItemLinkDetailSerializer
