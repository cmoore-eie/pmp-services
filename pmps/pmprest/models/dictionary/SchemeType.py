from django.db import models


class SchemeType(models.TextChoices):
    PRIVATE_SCHEME = "private", "Private"
    PUBLIC_SCHEME = "public", "Public"
    AFFINITY_SCHEME = "affinity", "Affinity"
    AGREEMENT_SCHEME = "agreement", "Agreement"
