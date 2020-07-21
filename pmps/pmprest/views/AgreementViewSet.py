from ..models.model.Agreement import Agreement
from ..serializers.AgreementSerializer import AgreementSerializer
from rest_framework import viewsets


class AgreementViewSet(viewsets.ModelViewSet):
    queryset = Agreement.objects.all()
    serializer_class = AgreementSerializer
