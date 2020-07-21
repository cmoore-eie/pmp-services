from drf_writable_nested import UniqueFieldsMixin, WritableNestedModelSerializer

from ..models.model.ContractVersion import ContractVersion
from ..serializers.ContractAttachmentSerializer import ContractAttachmentSerializer
from ..serializers.ContractCoverSerializer import ContractCoverSerializer


class ContractVersionSerializer(UniqueFieldsMixin, WritableNestedModelSerializer):

    contractAttachments = ContractAttachmentSerializer(many=True)
    contractCovers = ContractCoverSerializer(many=True)

    class Meta:
        model = ContractVersion
        fields = ['effectiveDate',
                  'expirationDate',
                  'itemIdentifier',
                  'ancestorItemIdentifier',
                  'purge',
                  'retired',
                  'versionNumber',
                  'hiddenContract',
                  'existence',
                  'contractAttachments',
                  'contractCovers', ]
