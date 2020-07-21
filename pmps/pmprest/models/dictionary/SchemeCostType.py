from django.db import models


class SchemeCostType(models.TextChoices):
    nocost = 'nocost', 'No Cost'
    discount = 'discount', 'Discount'
