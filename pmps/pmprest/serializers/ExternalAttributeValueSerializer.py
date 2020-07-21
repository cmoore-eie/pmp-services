from rest_framework import serializers
from ..models.model.ExternalAttributeValue import ExternalAttributeValue


class ExternalAttributeValueSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExternalAttributeValue
        fields = '__all__'

