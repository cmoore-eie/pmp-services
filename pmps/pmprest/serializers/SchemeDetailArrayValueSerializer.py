from rest_framework import serializers
from ..models.model.SchemeDetailArrayValue import SchemeDetailArrayValue


class SchemeDetailArrayValueSerializer(serializers.ModelSerializer):

    class Meta:
        model = SchemeDetailArrayValue
        fields = '__all__'

