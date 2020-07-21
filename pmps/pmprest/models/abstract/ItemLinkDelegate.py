from django.db import models


class ItemLinkDelegate(models.Model):
    itemIdentifier = models.CharField(max_length=255, primary_key=True)
    ancestorItemIdentifier = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        abstract = True
