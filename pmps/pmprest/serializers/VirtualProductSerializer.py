from django.core.exceptions import ObjectDoesNotExist
from drf_writable_nested import WritableNestedModelSerializer
from ..models.model.VirtualProduct import VirtualProduct
from ..models.model.VirtualProductCategory import VirtualProductCategory
from ..models.model.VirtualProductContract import VirtualProductContract
from ..models.model.VirtualProductFlavour import VirtualProductFlavour
from ..models.model.VirtualProductLine import VirtualProductLine
from .VirtualProductCategorySerializer import VirtualProductCategorySerializer
from .VirtualProductContractSerializer import VirtualProductContractSerializer
from .VirtualProductFlavourSerializer import VirtualProductFlavourSerializer
from .VirtualProductLineSerializer import VirtualProductLineSerializer
from ..utils.ChildType import ChildType
from ..utils.ChildUpdate import update_item


class VirtualProductSerializer(WritableNestedModelSerializer):
    virtualProductCategories = VirtualProductCategorySerializer(many=True)
    virtualProductContracts = VirtualProductContractSerializer(many=True)
    virtualProductFlavours = VirtualProductFlavourSerializer(many=True)
    virtualProductLines = VirtualProductLineSerializer(many=True)

    def update(self, instance, validated_data):
        category_data = validated_data.pop("virtualProductCategories")
        contract_data = validated_data.pop("virtualProductContracts")
        flavour_data = validated_data.pop("virtualProductFlavours")
        line_data = validated_data.pop("virtualProductLines")

        for field, value in validated_data.items():
            setattr(instance, field, value)

        update_item(instance, flavour_data, ChildType.VIRTUAL_PRODUCT_FLAVOUR)
        update_item(instance, line_data, ChildType.VIRTUAL_PRODUCT_LINE)
        update_item(instance, category_data, ChildType.VIRTUAL_PRODUCT_CATEGORY)
        update_item(instance, contract_data, ChildType.VIRTUAL_PRODUCT_CONTRACT)

        instance.save()

        return instance

    def create(self, validated_data):
        category_data = validated_data.pop("virtualProductCategories")
        contract_data = validated_data.pop("virtualProductContracts")
        flavour_data = validated_data.pop("virtualProductFlavours")
        line_data = validated_data.pop("virtualProductLines")
        virtual_product = VirtualProduct.objects.create(**validated_data)

        for category in category_data:
            VirtualProductCategory.objects.create(virtualProduct=virtual_product, **category)

        for contract in contract_data:
            VirtualProductContract.objects.create(virtualProduct=virtual_product, **contract)

        for flavour in flavour_data:
            VirtualProductFlavour.objects.create(virtualProduct=virtual_product, **flavour)

        for line in line_data:
            VirtualProductLine.objects.create(virtualProduct=virtual_product, **line)

        return virtual_product

    class Meta:
        model = VirtualProduct
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
                  'allowAffinity',
                  'allowCampaign',
                  'VirtualProductType',
                  'virtualProductCategories',
                  'virtualProductContracts',
                  'virtualProductFlavours',
                  'virtualProductLines', ]
