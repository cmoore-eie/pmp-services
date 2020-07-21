from rest_framework import serializers
from ..models.model.ItemLinkDefinitionDetail import ItemLinkDefinitionDetail


class ItemLinkDefinitionDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemLinkDefinitionDetail
        fields = '__all__'

