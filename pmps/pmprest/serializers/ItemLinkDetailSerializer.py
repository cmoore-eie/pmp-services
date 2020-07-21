from rest_framework import serializers
from ..models.model.ItemLinkDetail import ItemLinkDetail
from .ItemLinkDefinitionDetailSerializer import ItemLinkDefinitionDetailSerializer


class ItemLinkDetailSerializer(serializers.ModelSerializer):
    itemLinkDefinitionDetail = ItemLinkDefinitionDetailSerializer(many=False)

    class Meta:
        model = ItemLinkDetail
        fields = '__all__'
