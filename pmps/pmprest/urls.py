from django.urls import path, include
from rest_framework import routers

from .views.AgreementViewSet import AgreementViewSet
from .views.ConditionLogicViewSet import ConditionLogicViewSet
from .views.ContractViewSet import ContractViewSet
from .views.CoverageDependencyViewSet import CoverageDependencyViewSet
from .views.ExternalProductViewSet import ExternalProductViewSet
from .views.GeneralTermViewSet import GeneralTermViewSet
from .views.ItemLinkDefinitionViewSet import ItemLinkDefinitionViewSet
from .views.ItemLinkViewSet import ItemLinkViewSet
from .views.NegotiationViewSet import NegotiationViewSet
from .views.SchemeConditionViewSet import SchemeConditionViewSet
from .views.SchemeViewSet import SchemeViewSet
from .views.VirtualProductViewSet import VirtualProductViewSet

pmp_router = routers.DefaultRouter()
pmp_router.register(r'agreements', AgreementViewSet)
pmp_router.register(r'condition-logic', ConditionLogicViewSet)
pmp_router.register(r'contracts', ContractViewSet)
pmp_router.register(r'coverage-dependency', CoverageDependencyViewSet)
pmp_router.register(r'external-products', ExternalProductViewSet)
pmp_router.register(r'general-terms', GeneralTermViewSet)
pmp_router.register(r'item-links', ItemLinkViewSet)
pmp_router.register(r'item-link-definitions', ItemLinkDefinitionViewSet)
pmp_router.register(r'negotiations', NegotiationViewSet)
pmp_router.register(r'schemes', SchemeViewSet)
pmp_router.register(r'scheme-conditions', SchemeConditionViewSet)
pmp_router.register(r'virtual-products', VirtualProductViewSet)

urlpatterns = [
    path('', include(pmp_router.urls)),
]
