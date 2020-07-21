from django.db import models


class VirtualProductType(models.TextChoices):
    OPEN_VP = "open", "Open"
    CLOSED_VP = "closed", "Closed"
    AGREEMENT_VP = "generalagreement", "General Agreement"
