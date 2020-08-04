from rest_framework import serializers
from ..models.model.CoverageDependencyParent import CoverageDependencyParent


class CoverageDependencyParentSerializer(serializers.ModelSerializer):

    class Meta:
        model = CoverageDependencyParent
        fields = ['itemIdentifier',
                  'ancestorItemIdentifier',
                  'coverageCode',
                  'leftParenthesis',
                  'rightParenthesis',
                  'itemSequence',
                  'conditionLogic',
                  'coverageDependency', ]

