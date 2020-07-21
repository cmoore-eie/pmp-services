from rest_framework import serializers
from ..models.model.ExternalTermValue import ExternalTermValue


class ExternalTermValueSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExternalTermValue
        fields = '__all__'

