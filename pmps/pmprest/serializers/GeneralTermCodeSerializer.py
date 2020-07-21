from rest_framework import serializers
from ..models.model.GeneralTermCode import GeneralTermCode


class GeneralTermCodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = GeneralTermCode
        fields = '__all__'

