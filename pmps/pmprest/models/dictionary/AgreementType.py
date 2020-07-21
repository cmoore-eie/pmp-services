from django.db import models


class AgreementType(models.TextChoices):
    GeneralAgreement = "GeneralAgreement", "General Agreement"
    GeneralOffer = "GeneralOffer", "General Offer"
    RegularAgreement = "RegularAgreement", "Regular Agreement"
    CooperationAgreement = "CooperationAgreement", "Cooperation Agreement"
