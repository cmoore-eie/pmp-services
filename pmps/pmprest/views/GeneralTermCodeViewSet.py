from ..models.model.GeneralTermCode import GeneralTermCode
from ..serializers.GeneralTermCodeSerializer import GeneralTermCodeSerializer
from rest_framework import viewsets


class GeneralTermCodeViewSet(viewsets.ModelViewSet):
    queryset = GeneralTermCode.objects.all()
    serializer_class = GeneralTermCodeSerializer
