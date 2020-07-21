from rest_framework import serializers
from ..models.model.ItemLink import ItemLink
from .ItemLinkDetailSerializer import ItemLinkDetailSerializer


class ItemLinkSerializer(serializers.ModelSerializer):
    itemLinkDetails = ItemLinkDetailSerializer(many=True)

    class Meta:
        model = ItemLink
        fields = '__all__'

