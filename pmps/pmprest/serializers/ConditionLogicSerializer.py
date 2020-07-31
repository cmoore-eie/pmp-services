from rest_framework import serializers

from .ConditionLogicDetailSerializer import ConditionLogicDetailSerializer
from ..models.model.ConditionLogic import ConditionLogic


class ConditionLogicSerializer(serializers.ModelSerializer):
    conditionLogicDetails = ConditionLogicDetailSerializer(many=True)

    class Meta:
        model = ConditionLogic
        fields = ['effectiveDate',
                  'expirationDate',
                  'code',
                  'locked',
                  'jsonString',
                  'itemIdentifier',
                  'ancestorItemIdentifier',
                  'versionNumber',
                  'itemStatus',
                  'logicCode',
                  'name',
                  'productCode',
                  'conditionLogicDetails', ]

