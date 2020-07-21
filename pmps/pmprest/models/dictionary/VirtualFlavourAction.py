from django.db import models


class VirtualFlavourAction(models.TextChoices):
    STD_GRANDFATHERING = "grandfatherstd", "Standard Grandfathering"
    AS_IS_GRANDFATHERING = "grandfatherasis", "As Is Grandfathering"
