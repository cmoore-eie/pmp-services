from rest_framework import serializers
from ..models.model.ConditionLogicDetail import ConditionLogicDetail


class ConditionLogicDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConditionLogicDetail
        fields = ['itemIdentifier',
                  'ancestorItemIdentifier',
                  'conditionLogic', ]

