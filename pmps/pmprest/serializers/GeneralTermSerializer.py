from rest_framework import serializers
from ..models.model.GeneralTerm import GeneralTerm
from ..serializers.GeneralTermCodeSerializer import GeneralTermCodeSerializer


class GeneralTermSerializer(serializers.ModelSerializer):
    generalTermCodes = GeneralTermCodeSerializer(many=True)

    class Meta:
        model = GeneralTerm
        fields = '__all__'

