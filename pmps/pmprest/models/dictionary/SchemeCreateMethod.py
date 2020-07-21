from django.db import models


class SchemeCreateMethod(models.TextChoices):
    MANUAL = "manual", "Manual"
    NEGOTIATION = "negotiationgenerates", "Negotiation Generated"
