from django.db import models


class EffectiveExpirationDate(models.Model):
    effectiveDate = models.CharField(max_length=20, null=False)
    expirationDate = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        abstract = True
