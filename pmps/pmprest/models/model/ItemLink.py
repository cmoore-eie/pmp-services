from django.db import models


class ItemLink(models.Model):
    #
    # Parent Values
    #
    parentType = models.CharField(max_length=255, blank=True)
    parentCode = models.CharField(max_length=255, blank=True)
    parentSubCode = models.CharField(max_length=255, blank=True)
    parentVersionNumber = models.IntegerField(null=True)
    parentItemIdentifier = models.CharField(max_length=255, blank=True)
    parentSecondaryIdentifier = models.CharField(max_length=255, blank=True)
    parentPublicID = models.CharField(max_length=255, blank=True)
    #
    # Child Values
    #
    childType = models.CharField(max_length=255, blank=True)
    childCode = models.CharField(max_length=255, blank=True)
    childSubCode = models.CharField(max_length=255, blank=True)
    childVersionNumber = models.IntegerField(null=True)
    childItemIdentifier = models.CharField(max_length=255, blank=True)
    childSecondaryIdentifier = models.CharField(max_length=255, blank=True)
    childPublicID = models.CharField(max_length=255, blank=True)
    #
    # Other
    #
    removed = models.BooleanField()
    objects = models.Manager()

    def __str__(self):
        return f'{self.ParentType} - {self.ParentItemIdentifier}'
