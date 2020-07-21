from django.db import models


class Currency(models.TextChoices):
    gbp = 'gbp', "GBP"
    usd = 'usd', 'USD'
    eur = 'euro', 'Euro'
