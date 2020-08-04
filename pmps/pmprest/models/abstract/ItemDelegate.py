from django.db import models


class ItemDelegate(models.Model):
    code = models.CharField(max_length=50)
    locked = models.BooleanField(default=False)
    jsonString = models.TextField(null=True, blank=True)
    create_time = models.DateTimeField(null=True, blank=True)
    update_time = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True
