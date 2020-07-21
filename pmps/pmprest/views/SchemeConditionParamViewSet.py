from ..models.model.SchemeConditionParam import SchemeConditionParam
from ..serializers.SchemeConditionParamSerializer import SchemeConditionParamSerializer
from rest_framework import viewsets


class SchemeConditionParamViewSet(viewsets.ModelViewSet):
    queryset = SchemeConditionParam.objects.all()
    serializer_class = SchemeConditionParamSerializer
