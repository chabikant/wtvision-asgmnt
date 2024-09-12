from django.db import models
from django.utils import timezone
import uuid

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Items(BaseModel):
    key = models.CharField(max_length=50, blank=False, null=False)
    value = models.TextField()

    def __str__(self):
        return self.key
