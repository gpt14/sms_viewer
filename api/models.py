from datetime import timedelta
import uuid

import django
from django.db import models
from django.utils import timezone


class SmsManager(models.Manager):
    def get_queryset(self):
        min_time = timezone.now() - timedelta(minutes=5)
        return super().get_queryset().filter(created_at__gte=min_time)


# Create your models here.
class Sms(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone_number = models.CharField(max_length=12)
    sms_body = models.CharField(max_length=500)
    created_at = models.DateTimeField(editable=False, default=timezone.now)
    valid_sms = SmsManager()

    class Meta:
        ordering = ['-created_at', ]

    def __str__(self):
        return self.sms_body
