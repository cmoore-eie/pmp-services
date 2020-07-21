from rest_framework import serializers
from ..models.model.SchemeDetailParam import SchemeDetailParam
from .SchemeConditionParamSerializer import SchemeConditionParamSerializer


class SchemeDetailParamSerializer(serializers.ModelSerializer):

    class Meta:
        model = SchemeDetailParam
        fields = ['itemIdentifier',
                  'ancestorItemIdentifier',
                  'stringValue',
                  'booleanValue',
                  'dateValue',
                  'integerValue',
                  'decimalValue',
                  'moneyValue',
                  'schemeCalcValueType',
                  'schemeConditionParam',
                  'schemeDetail', ]
