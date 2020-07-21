from rest_framework import serializers
from ..models.model.ItemLinkDefinition import ItemLinkDefinition
from ..serializers.ItemLinkDefinitionDetailSerializer import ItemLinkDefinitionDetailSerializer


class ItemLinkDefinitionSerializer(serializers.ModelSerializer):
    itemLinkDefinitionDetails = ItemLinkDefinitionDetailSerializer(many=True)

    class Meta:
        model = ItemLinkDefinition
        fields = '__all__'

