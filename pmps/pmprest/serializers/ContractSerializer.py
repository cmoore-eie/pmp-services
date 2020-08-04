from datetime import datetime

from django.core.exceptions import ObjectDoesNotExist
from drf_writable_nested import WritableNestedModelSerializer

from .ContractVersionSerializer import ContractVersionSerializer
from ..models.model.Contract import Contract
from ..models.model.ContractAttachment import ContractAttachment
from ..models.model.ContractCover import ContractCover
from ..models.model.ContractVersion import ContractVersion
from ..utils.ChildType import ChildType
from ..utils.ChildUpdate import update_item


class ContractSerializer(WritableNestedModelSerializer):
    contractVersions = ContractVersionSerializer(many=True)

    def update(self, instance, validated_data):
        version_data = validated_data.pop("contractVersions")

        for field, value in validated_data.items():
            setattr(instance, field, value)

        for version in version_data:
            version_list = dict(version)  # Convert the OrderDict to plain dict to enable the information to be processed
            attachment_data = version_list.pop('contractAttachments')
            cover_data = version_list.pop('contractCovers')
            item_instance = update_item(instance, [version_list], ChildType.CONTRACT_VERSION)  # Data must be a list hence []
            update_item(item_instance, attachment_data, ChildType.CONTRACT_ATTACHMENT)
            update_item(item_instance, cover_data, ChildType.CONTRACT_COVER)

        instance.save()

        return instance

    def create(self, validated_data):
        version_data = validated_data.pop("contractVersions")
        contract_item = Contract.objects.create(**validated_data)
        for version in version_data:
            '''
            version_data at this point is an orderdict, this is converted to a standard dict and then
            processed. 
            '''
            version_list = dict(version)
            attachment_data = version_list.pop('contractAttachments')
            cover_data = version_list.pop('contractCovers')
            new_version = ContractVersion.objects.create(contract=contract_item, **version_list)

            for attach_item in attachment_data:
                ContractAttachment.objects.create(contractVersion=new_version, **attach_item)

            for cover_item in cover_data:
                ContractCover.objects.create(contractVersion=new_version, **cover_item)

        return contract_item

    class Meta:
        model = Contract
        fields = ['code',
                  'locked',
                  'jsonString',
                  'itemIdentifier',
                  'ancestorItemIdentifier',
                  'versionNumber',
                  'itemStatus',
                  'name',
                  'productCode',
                  'contractVersions',
                  'create_time',
                  'update_time', ]
