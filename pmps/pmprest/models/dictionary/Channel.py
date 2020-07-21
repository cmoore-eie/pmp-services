from django.db import models


class Channel(models.TextChoices):
    digital = 'digital', 'Digital'
    callcenter = 'callcenter' 'Call Center'
    agent = 'agent', 'Agent'
    broker = 'broker', 'Broker'
    document = 'document', 'Document'
