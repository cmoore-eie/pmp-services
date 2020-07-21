from django.db import models


class ItemLinkDetail(models.Model):
    itemLink = models.ForeignKey('ItemLink', on_delete=models.CASCADE, related_name='itemLinkDetails')
    itemLinkDefinitionDetail = models.ForeignKey('ItemLinkDefinitionDetail', on_delete=models.CASCADE, related_name='itemLinkDefinitionDetail')
    value = models.CharField(max_length=255, blank=True)
    objects = models.Manager()

    def __str__(self):
        return f'{self.ItemLinkDefinitionDetail.name}'
