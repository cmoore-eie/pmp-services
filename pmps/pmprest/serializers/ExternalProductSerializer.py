from rest_framework import serializers
from ..models.model.ExternalProduct import ExternalProduct
from ..serializers.ExternalAttributeValueSerializer import ExternalAttributeValueSerializer
from ..serializers.ExternalTermValueSerializer import ExternalTermValueSerializer


class ExternalProductSerializer(serializers.ModelSerializer):
    externalAttributeValues = ExternalAttributeValueSerializer(many=True)
    externalTermValues = ExternalTermValueSerializer(many=True)

    class Meta:
        model = ExternalProduct
        fields = '__all__'

