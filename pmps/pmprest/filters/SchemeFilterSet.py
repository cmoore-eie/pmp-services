import django_filters

from ..models.model.Scheme import Scheme


class SchemeFilterSet(django_filters.FilterSet):
    with_identifier = django_filters.CharFilter(field_name='itemIdentifier', lookup_expr='exact')
    with_code = django_filters.CharFilter(field_name='code', lookup_expr='exact')
    with_name = django_filters.CharFilter(field_name='name', lookup_expr='exact')
    with_productCode = django_filters.CharFilter(field_name='productCode', lookup_expr='exact')

    class Meta:
        model = Scheme
        fields = ['with_code',
                  'with_name',
                  'with_identifier',
                  'with_productCode', ]
