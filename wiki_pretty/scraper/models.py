import uuid
from django.db import models

# Create your models here.
class Wiki(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    content = models.CharField
    name = models.CharField(max_length=100)
