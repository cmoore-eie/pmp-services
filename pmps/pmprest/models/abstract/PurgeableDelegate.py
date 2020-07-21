from django.db import models

'''
This abstract class is added to models that require to have the purge or retire flags
for additional processing of the object.
'''


class PurgeableDelegate(models.Model):
    purge = models.BooleanField(default=False)
    retired = models.BooleanField(default=False)

    class Meta:
        abstract = True
