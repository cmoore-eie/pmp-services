from django.db import models


class AgreementStatus(models.TextChoices):
    new = "new", "New"
    withdrawn = "withdrawn", "Withdrawn"
    bound = "bound", "Bound"
    canceled = "canceled", "Canceled"
    negotiated = "negotiated", "Negotiated"
    finished = "finished", "Finished"
