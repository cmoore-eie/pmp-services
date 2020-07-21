from django.db import models


class SchemeValidationType(models.TextChoices):
    atmost = 'atmost', 'At Most'
    atleast = 'atleast', 'At Least'
    exactly = 'exactly', 'exactly'
