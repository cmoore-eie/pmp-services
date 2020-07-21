from ..models.model.SchemeCondition import SchemeCondition
from ..serializers.SchemeConditionSerializer import SchemeConditionSerializer
from rest_framework import viewsets


class SchemeConditionViewSet(viewsets.ModelViewSet):
    queryset = SchemeCondition.objects.all()
    serializer_class = SchemeConditionSerializer
