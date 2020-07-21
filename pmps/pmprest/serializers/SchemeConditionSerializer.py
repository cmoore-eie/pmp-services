from rest_framework import serializers
from ..models.model.SchemeCondition import SchemeCondition
from .SchemeConditionParamSerializer import SchemeConditionParamSerializer


class SchemeConditionSerializer(serializers.ModelSerializer):
    conditionParams = SchemeConditionParamSerializer(many=True)

    class Meta:
        model = SchemeCondition
        fields = ['effectiveDate',
                  'expirationDate',
                  'code',
                  'locked',
                  'jsonString',
                  'itemIdentifier',
                  'ancestorItemIdentifier',
                  'versionNumber',
                  'itemStatus',
                  'name',
                  'condition',
                  'producerCode',
                  'root',
                  'description',
                  'conditionParams', ]

