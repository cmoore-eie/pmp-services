from django.db import models


class SchemeOperatorType(models.TextChoices):
    equals = 'equals', 'Equals'
    lassthan = 'lessthan', 'Less Than'
    greaterthan = 'greaterthan', 'Greater Than'
