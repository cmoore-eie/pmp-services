from drf_writable_nested import UniqueFieldsMixin
from rest_framework import serializers
from ..models.model.VirtualProductLine import VirtualProductLine


class VirtualProductLineSerializer(UniqueFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = VirtualProductLine
        fields = '__all__'

