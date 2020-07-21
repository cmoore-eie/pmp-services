from rest_framework import serializers
from ..models.model.Agreement import Agreement


class AgreementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Agreement
        fields = '__all__'
