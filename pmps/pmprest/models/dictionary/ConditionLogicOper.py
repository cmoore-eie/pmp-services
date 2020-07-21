from django.db import models


class ConditionLogicOper(models.TextChoices):
    andOper = "and", "And"
    orOper = "or", "Or"
    notOper = "not" "Not"
