from django.db import models


class ItemStatus(models.TextChoices):
    DRAFT = "draft", "Draft"
    STAGE = "stage", "Stage"
    APPROVED = "approved", "Approved"
