from ..models.model.SchemeDetail import SchemeDetail
from ..serializers.SchemeDetailSerializer import SchemeDetailSerializer
from rest_framework import viewsets


class SchemeDetailViewSet(viewsets.ModelViewSet):
    queryset = SchemeDetail.objects.all()
    serializer_class = SchemeDetailSerializer
