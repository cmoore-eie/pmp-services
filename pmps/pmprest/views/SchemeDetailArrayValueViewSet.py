from ..models.model.SchemeDetailArrayValue import SchemeDetailArrayValue
from ..serializers.SchemeDetailArrayValueSerializer import SchemeDetailArrayValueSerializer
from rest_framework import viewsets


class SchemeDetailArrayValueViewSet(viewsets.ModelViewSet):
    queryset = SchemeDetailArrayValue.objects.all()
    serializer_class = SchemeDetailArrayValueSerializer
