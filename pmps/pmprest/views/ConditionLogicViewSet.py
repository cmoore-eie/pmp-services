from ..models.model.ConditionLogic import ConditionLogic
from ..serializers.ConditionLogicSerializer import ConditionLogicSerializer
from rest_framework import viewsets


class ConditionLogicViewSet(viewsets.ModelViewSet):
    queryset = ConditionLogic.objects.all()
    serializer_class = ConditionLogicSerializer
