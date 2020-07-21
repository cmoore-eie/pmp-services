from drf_writable_nested import UniqueFieldsMixin
from rest_framework import serializers
from ..models.model.VirtualProductContract import VirtualProductContract
from ..models.model.Contract import Contract


class VirtualProductContractSerializer(UniqueFieldsMixin, serializers.ModelSerializer):
    
    def create(self, validated_data):
        virtual_product_contract = VirtualProductContract.objects.create(**validated_data)

        if virtual_product_contract.contractIdentifier is not None:
            contract = Contract.objects.get(pk=virtual_product_contract.contractIdentifier)
            virtual_product_contract.contract = contract

        return virtual_product_contract

    class Meta:
        model = VirtualProductContract
        fields = '__all__'

