from rest_framework import serializers
from ..models.model.NegotiationSection import NegotiationSection
from .NegotiationDetailSerializer import NegotiationDetailSerializer


class NegotiationSectionSerializer(serializers.ModelSerializer):
    negotiationDetails = NegotiationDetailSerializer(many=True)

    class Meta:
        model = NegotiationSection
        fields = '__all__'

