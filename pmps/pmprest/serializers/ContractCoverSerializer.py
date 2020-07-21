from drf_writable_nested import UniqueFieldsMixin
from rest_framework import serializers
from ..models.model.ContractCover import ContractCover


class ContractCoverSerializer(UniqueFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = ContractCover
        fields = '__all__'

