from django.db import models


class ItemLinkDefinition(models.Model):
    identifier = models.CharField(max_length=255, blank=True)
    objects = models.Manager()

    def __str__(self):
        return f'{self.Identifier}'
