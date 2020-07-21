from django.db import models


class NegotiationStatus(models.TextChoices):
    inprogress = 'inprogress', 'Inprogress'
    accepted = 'accepted', 'Accepted'
    cancelled = 'cancelled', 'Cancelled'