from django.db import models


class GeneralTermAttachment(models.TextChoices):
    Policy = 'policy', 'Policy'
    Line = 'line', 'Line'
