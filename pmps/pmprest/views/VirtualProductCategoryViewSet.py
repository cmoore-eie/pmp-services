from ..models.model.VirtualProductCategory import VirtualProductCategory
from ..serializers.VirtualProductCategorySerializer import VirtualProductCategorySerializer
from rest_framework import viewsets


class VirtualProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = VirtualProductCategory.objects.all()
    serializer_class = VirtualProductCategorySerializer
