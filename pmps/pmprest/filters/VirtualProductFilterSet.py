import django_filters

from ..models.model.VirtualProduct import VirtualProduct


class VirtualProductFilterSet(django_filters.FilterSet):
    with_identifier = django_filters.CharFilter(field_name='itemIdentifier', lookup_expr='exact')
    with_code = django_filters.CharFilter(field_name='code', lookup_expr='exact')
    with_productCode = django_filters.CharFilter(field_name='productCode', lookup_expr='exact')
    with_effectiveDate = django_filters.DateFilter(field_name='effectiveDate', lookup_expr='gte')
    with_expirationDate = django_filters.DateFilter(field_name='expirationDate', lookup_expr='lte')
    with_versionNumber = django_filters.NumberFilter(field_name='versionNumber', lookup_expr='exact')
    with_itemStatus = django_filters.CharFilter(field_name='itemStatus', lookup_expr='exact')
    with_VirtualProductType = django_filters.CharFilter(field_name='VirtualProductType', lookup_expr='exact')

    class Meta:
        model = VirtualProduct
        fields = ['with_effectiveDate',
                  'with_expirationDate',
                  'with_code',
                  'with_identifier',
                  'with_versionNumber',
                  'with_itemStatus',
                  'with_productCode',
                  'with_VirtualProductType', ]
