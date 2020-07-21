from ..filters.SchemeFilterSet import SchemeFilterSet
from ..models.model.Scheme import Scheme
from ..serializers.SchemeSerializer import SchemeSerializer
from rest_framework import viewsets


class SchemeViewSet(viewsets.ModelViewSet):
    queryset = Scheme.objects.all()
    serializer_class = SchemeSerializer
    filterset_class = SchemeFilterSet
