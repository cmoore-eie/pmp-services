from drf_writable_nested import WritableNestedModelSerializer, UniqueFieldsMixin
from ..models.model.SchemeDetail import SchemeDetail
from .SchemeDetailParamSerializer import SchemeDetailParamSerializer
from .SchemeDetailArrayValueSerializer import SchemeDetailArrayValueSerializer


class SchemeDetailSerializer(UniqueFieldsMixin, WritableNestedModelSerializer):
    schemeDetailParams = SchemeDetailParamSerializer(many=True)
    schemeDetailArrayValues = SchemeDetailArrayValueSerializer(many=True)

    class Meta:
        model = SchemeDetail
        fields = ['itemIdentifier',
                  'ancestorItemIdentifier',
                  'stringValue',
                  'booleanValue',
                  'dateValue',
                  'integerValue',
                  'decimalValue',
                  'moneyValue',
                  'schemeCalcValueType',
                  'comparator',
                  'parentCode',
                  'condition',
                  'forceValue',
                  'timeDuration',
                  'costDiscount',
                  'minMax',
                  'currency',
                  'schemeCostType',
                  'schemeOperatorType',
                  'schemeSourceType',
                  'schemeTimeframe',
                  'schemeValueType',
                  'schemeValidationType',
                  'scheme',
                  'schemeDetailParams',
                  'schemeDetailArrayValues', ]
