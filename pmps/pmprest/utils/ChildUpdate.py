from django.core.exceptions import ObjectDoesNotExist

from ..models.model.ContractAttachment import ContractAttachment
from ..models.model.ContractCover import ContractCover
from ..models.model.ContractVersion import ContractVersion
from ..models.model.SchemeDetail import SchemeDetail
from ..models.model.SchemeDetailArrayValue import SchemeDetailArrayValue
from ..models.model.SchemeDetailParam import SchemeDetailParam
from ..models.model.VirtualProductCategory import VirtualProductCategory
from ..models.model.VirtualProductContract import VirtualProductContract
from ..models.model.VirtualProductFlavour import VirtualProductFlavour
from ..models.model.VirtualProductLine import VirtualProductLine

get_types = {'ContractVersion': ContractVersion,
             'ContractAttachment': ContractAttachment,
             'ContractCover': ContractCover,
             'VirtualProductFlavour': VirtualProductFlavour,
             'VirtualProductLine': VirtualProductLine,
             'VirtualProductCategory': VirtualProductCategory,
             'VirtualProductContract': VirtualProductContract,
             'SchemeDetail': SchemeDetail,
             'SchemeDetailArrayValue': SchemeDetailArrayValue,
             'SchemeDetailParam': SchemeDetailParam,
             }

update_types = {'ContractVersion': lambda i, d: ContractVersion.objects.create(contract=i, **d),
                'ContractAttachment': lambda i, d: ContractAttachment.objects.create(contractVersion=i, **d),
                'ContractCover': lambda i, d: ContractCover.objects.create(contractVersion=i, **d),
                'VirtualProductFlavour': lambda i, d: VirtualProductFlavour.objects.create(virtualProduct=i, **d),
                'VirtualProductLine': lambda i, d: VirtualProductLine.objects.create(virtualProduct=i, **d),
                'VirtualProductCategory': lambda i, d: VirtualProductCategory.objects.create(virtualProduct=i, **d),
                'VirtualProductContract': lambda i, d: VirtualProductContract.objects.create(virtualProduct=i, **d),
                'SchemeDetail': lambda i, d: SchemeDetail.objects.create(scheme=i, **d),
                'SchemeDetailArrayValue': lambda i, d: SchemeDetailArrayValue.objects.create(SchemeDetail=i, **d),
                'SchemeDetailParam': lambda i, d: SchemeDetailParam.objects.create(schemeDetail=i, **d),
                }


def update_item(instance, data_list, item_type):
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
