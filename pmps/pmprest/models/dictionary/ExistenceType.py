from django.db import models


class ExistenceType(models.TextChoices):
    Required = "Required", "Required"
    Suggested = "Suggested", "Suggested"
    Electable = "Electable", "Electable"
