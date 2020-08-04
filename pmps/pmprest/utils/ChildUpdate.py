from django.core.exceptions import ObjectDoesNotExist

from .ChildType import ChildType
from ..models.model.ConditionLogicDetail import ConditionLogicDetail
from ..models.model.ContractAttachment import ContractAttachment
from ..models.model.ContractCover import ContractCover
from ..models.model.ContractVersion import ContractVersion
from ..models.model.CoverageDependencyChild import CoverageDependencyChild
from ..models.model.CoverageDependencyParent import CoverageDependencyParent
from ..models.model.CoverageDependencySelect import CoverageDependencySelect
from ..models.model.ExternalAttributeValue import ExternalAttributeValue
from ..models.model.ExternalTermValue import ExternalTermValue
from ..models.model.SchemeDetail import SchemeDetail
from ..models.model.SchemeDetailArrayValue import SchemeDetailArrayValue
from ..models.model.SchemeDetailParam import SchemeDetailParam
from ..models.model.VirtualProductCategory import VirtualProductCategory
from ..models.model.VirtualProductContract import VirtualProductContract
from ..models.model.VirtualProductFlavour import VirtualProductFlavour
from ..models.model.VirtualProductLine import VirtualProductLine


class ExternalAttributeTerm(object):
    pass


get_types = {ChildType.CONDITION_LOGIC_DETAIL: ConditionLogicDetail,
             ChildType.CONTRACT_ATTACHMENT: ContractAttachment,
             ChildType.CONTRACT_COVER: ContractCover,
             ChildType.CONTRACT_VERSION: ContractVersion,
             ChildType.COVERAGE_DEPENDENCY_CHILD: CoverageDependencyChild,
             ChildType.COVERAGE_DEPENDENCY_PARENT: CoverageDependencyParent,
             ChildType.COVERAGE_DEPENDENCY_SELECT: CoverageDependencySelect,
             ChildType.EXTERNAL_ATTRIBUTE_VALUE: ExternalAttributeValue,
             ChildType.EXTERNAL_TERM_VALUE: ExternalTermValue,
             ChildType.VIRTUAL_PRODUCT_FLAVOUR: VirtualProductFlavour,
             ChildType.VIRTUAL_PRODUCT_LINE: VirtualProductLine,
             ChildType.VIRTUAL_PRODUCT_CATEGORY: VirtualProductCategory,
             ChildType.VIRTUAL_PRODUCT_CONTRACT: VirtualProductContract,
             ChildType.SCHEME_DETAIL: SchemeDetail,
             ChildType.SCHEME_DETAIL_ARRAY_VALUE: SchemeDetailArrayValue,
             ChildType.SCHEME_DETAIL_PARAM: SchemeDetailParam,
             }

update_types = {ChildType.CONDITION_LOGIC_DETAIL: lambda i, d: ConditionLogicDetail.objects.create(contract=i, **d),
                ChildType.CONTRACT_ATTACHMENT: lambda i, d: ContractAttachment.objects.create(contractVersion=i, **d),
                ChildType.CONTRACT_COVER: lambda i, d: ContractCover.objects.create(contractVersion=i, **d),
                ChildType.CONTRACT_VERSION: lambda i, d: ContractVersion.objects.create(contract=i, **d),
                ChildType.COVERAGE_DEPENDENCY_CHILD: lambda i, d: CoverageDependencyChild.objects.create(contract=i, **d),
                ChildType.COVERAGE_DEPENDENCY_PARENT: lambda i, d: CoverageDependencyParent.objects.create(contract=i, **d),
                ChildType.COVERAGE_DEPENDENCY_SELECT: lambda i, d: CoverageDependencySelect.objects.create(contract=i, **d),
                ChildType.EXTERNAL_ATTRIBUTE_VALUE: lambda i, d: ExternalAttributeValue.objects.create(contract=i, **d),
                ChildType.EXTERNAL_TERM_VALUE: lambda i, d: ExternalTermValue.objects.create(contract=i, **d),
                ChildType.VIRTUAL_PRODUCT_FLAVOUR: lambda i, d: VirtualProductFlavour.objects.create(virtualProduct=i, **d),
                ChildType.VIRTUAL_PRODUCT_LINE: lambda i, d: VirtualProductLine.objects.create(virtualProduct=i, **d),
                ChildType.VIRTUAL_PRODUCT_CATEGORY: lambda i, d: VirtualProductCategory.objects.create(virtualProduct=i, **d),
                ChildType.VIRTUAL_PRODUCT_CONTRACT: lambda i, d: VirtualProductContract.objects.create(virtualProduct=i, **d),
                ChildType.SCHEME_DETAIL: lambda i, d: SchemeDetail.objects.create(scheme=i, **d),
                ChildType.SCHEME_DETAIL_ARRAY_VALUE: lambda i, d: SchemeDetailArrayValue.objects.create(SchemeDetail=i, **d),
                ChildType.SCHEME_DETAIL_PARAM: lambda i, d: SchemeDetailParam.objects.create(schemeDetail=i, **d),
                }


def update_item(instance, data_list, item_type: ChildType):
    item_type_class = get_types.get(item_type)
    lambda_update_function = update_types.get(item_type)
    for data in data_list:
        '''
        As it is not possible to say that the absence is an indication of deletion for child objects
        they are marked for purge. This is picked up and the object deleted from the database. If the 
        object can not be found no error processing takes place as could be a new object added then marked
        for purge without it being saved to the database.
        '''
        if data.get('purge') is True:
            try:
                delete_item = item_type_class.objects.get(pk=data.get('itemIdentifier'))
                delete_item.delete()
            except ObjectDoesNotExist:
                pass
        else:
            '''
            Updating of the child will look to extract the child from the database, if this is not possible 
            as the child maybe new then it is created and stored in the database. If this is an update the 
            field and value are taken from the dict and used to set the attribute of the retrieved object.
            '''
            try:
                item_instance = item_type_class.objects.get(pk=data.get('itemIdentifier'))
                for field, value in data.items():
                    setattr(item_instance, field, value)
            except ObjectDoesNotExist:
                item_instance = lambda_update_function(instance, data)

            item_instance.save()
            return item_instance
