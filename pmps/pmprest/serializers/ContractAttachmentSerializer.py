from drf_writable_nested import UniqueFieldsMixin
from rest_framework import serializers
from ..models.model.ContractAttachment import ContractAttachment


class ContractAttachmentSerializer(UniqueFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = ContractAttachment
        fields = '__all__'

