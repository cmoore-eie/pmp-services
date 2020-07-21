from rest_framework import serializers
from ..models.model.NegotiationDetail import NegotiationDetail


class NegotiationDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = NegotiationDetail
        fields = '__all__'

