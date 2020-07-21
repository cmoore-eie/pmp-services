from django.db import models
from ..abstract.EffectiveExpirationDate import EffectiveExpirationDate
from ..abstract.ItemStatusDelegate import ItemStatusDelegate
from ..abstract.ItemLinkDelegate import ItemLinkDelegate
from ..abstract.ItemDelegate import ItemDelegate
from ..dictionary.AgreementCancelReason import AgreementCancelReason
from ..dictionary.AgreementStatus import AgreementStatus
from ..dictionary.AgreementType import AgreementType


class Agreement(EffectiveExpirationDate, ItemStatusDelegate, ItemLinkDelegate, ItemDelegate):
    name = models.CharField(max_length=255, blank=True)
    agreementNumber = models.CharField(max_length=50, blank=True)
    acceptanceDate = models.DateField(null=True)
    description = models.CharField(max_length=255, blank=True)
    customerAgreementNo = models.CharField(max_length=255, blank=True)
    canceledDate = models.DateField(null=True)
    cancelReasonDesc = models.CharField(max_length=255, blank=True)
    objects = models.Manager()

    cancelReason = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        choices=AgreementCancelReason.choices)

    agreementStatus = models.CharField(
        max_length=20,
        choices=AgreementStatus.choices,
        default=AgreementStatus.new)

    agreementType = models.CharField(
        max_length=20,
        choices=AgreementType.choices,
        default=AgreementType.GeneralAgreement)
