from ..models.model.ConditionLogicDetail import ConditionLogicDetail
from ..serializers.ConditionLogicDetailSerializer import  ConditionLogicDetailSerializer
from rest_framework import viewsets


class ConditionLogicDetailViewSet(viewsets.ModelViewSet):
    queryset = ConditionLogicDetail.objects.all()
    serializer_class = ConditionLogicDetailSerializer
