from ..models.model.SchemeDetailParam import SchemeDetailParam
from ..serializers.SchemeDetailParamSerializer import SchemeDetailParamSerializer
from rest_framework import viewsets


class SchemeDetailParamViewSet(viewsets.ModelViewSet):
    queryset = SchemeDetailParam.objects.all()
    serializer_class = SchemeDetailParamSerializer
