from rest_framework import serializers

from .ConditionLogicDetailSerializer import ConditionLogicDetailSerializer
from ..models.model.ConditionLogic import ConditionLogic


class ConditionLogicSerializer(serializers.ModelSerializer):
    ConditionLogicDetails = ConditionLogicDetailSerializer(many=True)

    class Meta:
        model = ConditionLogic
        fields = '__all__'

