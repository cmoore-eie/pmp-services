from rest_framework import serializers
from ..models.model.Negotiation import Negotiation
from .NegotiationSectionSerializer import NegotiationSectionSerializer


class NegotiationSerializer(serializers.ModelSerializer):
    negotiationSections = NegotiationSectionSerializer(many=True)

    class Meta:
        model = Negotiation
        fields = '__all__'

