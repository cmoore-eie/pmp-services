from django.db import models


class AgreementCancelReason(models.TextChoices):
    cancel_by_carrier = 'cancel_by_carrier', 'Cancelled by Carrier'
    cancel_by_client = 'cancel_by_client', 'Cancelled by Client'
    mutual_agreement = 'mutual_agreement', 'Mutual agreement'
