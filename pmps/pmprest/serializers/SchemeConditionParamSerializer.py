from rest_framework import serializers
from ..models.model.SchemeConditionParam import SchemeConditionParam


class SchemeConditionParamSerializer(serializers.ModelSerializer):

    class Meta:
        model = SchemeConditionParam
        fields = '__all__'

