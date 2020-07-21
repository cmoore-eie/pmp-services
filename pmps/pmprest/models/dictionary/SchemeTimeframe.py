from django.db import models


class SchemeTimeframe(models.TextChoices):
    days = 'days', 'Days'
    weeks = 'weeks', 'Weeks'
    months = 'months', 'Months'
    years = 'years', 'Years'
