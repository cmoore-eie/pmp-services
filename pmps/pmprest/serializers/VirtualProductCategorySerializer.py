from drf_writable_nested import UniqueFieldsMixin
from rest_framework import serializers
from ..models.model.VirtualProductCategory import VirtualProductCategory


class VirtualProductCategorySerializer(UniqueFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = VirtualProductCategory
        fields = '__all__'

