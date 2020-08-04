from drf_writable_nested import WritableNestedModelSerializer
from ..models.model.Scheme import Scheme
from ..models.model.SchemeDetail import SchemeDetail
from .SchemeDetailSerializer import SchemeDetailSerializer
from ..models.model.SchemeDetailArrayValue import SchemeDetailArrayValue
from ..models.model.SchemeDetailParam import SchemeDetailParam
from ..utils.ChildType import ChildType
from ..utils.ChildUpdate import update_item


class SchemeSerializer(WritableNestedModelSerializer):
    schemeDetails = SchemeDetailSerializer(many=True)

    def update(self, instance, validated_data):
        child_data = validated_data.pop("schemeDetails")

        for field, value in validated_data.items():
            setattr(instance, field, value)

        for child in child_data:
            child_list = dict(child)  # Convert the OrderDict to plain dict to enable the information to be processed
            param_data = child_list.pop('schemeDetailParams')
            array_data = child_list.pop('schemeDetailArrayValues')
            item_instance = update_item(instance, [child_list], ChildType.SCHEME_DETAIL)  # Data must be a list hence []
            update_item(item_instance, param_data, ChildType.SCHEME_DETAIL_PARAM)
            update_item(item_instance, array_data, ChildType.SCHEME_DETAIL_ARRAY_VALUE)

        instance.save()

        return instance

    def create(self, validated_data):
        detail_data = validated_data.pop("schemeDetails")
        scheme = Scheme.objects.create(**validated_data)

        for detail in detail_data:
            detail_list = dict(detail)
            array_data = detail_list.pop("schemeDetailArrayValues")
            param_data = detail_list.pop("schemeDetailParams")
            new_detail = SchemeDetail.objects.create(scheme=scheme, **detail_list)
            for array_detail in array_data:
                SchemeDetailArrayValue.objects.create(schemeDetail=new_detail, **array_detail)

            for param_detail in param_data:
                SchemeDetailParam.objects.create(schemeDetail=new_detail, **param_detail)

        return scheme

    class Meta:
        model = Scheme
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
                  'productCode',
                  'renewalAvailable',
                  'autoImportDate',
                  'description',
                  'private',
                  'schemeType',
                  'createMethod',
                  'schemeDetails', ]
