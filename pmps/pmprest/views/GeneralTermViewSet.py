from ..models.model.GeneralTerm import GeneralTerm
from ..serializers.GeneralTermSerializer import GeneralTermSerializer
from rest_framework import viewsets


class GeneralTermViewSet(viewsets.ModelViewSet):
    queryset = GeneralTerm.objects.all()
    serializer_class = GeneralTermSerializer
