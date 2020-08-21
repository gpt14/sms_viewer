from datetime import timedelta

from django.db import models
from django.utils import timezone


class SmsManager(models.Manager):
    def get_queryset(self):
        # return super().get_quesyset().filter(self.model, using=self._db)
        # return self.filter(created_date__gte=min_time)
        min_time = timezone.now() - timedelta(minutes=30)
        return super().get_queryset().filter(created_at__gte=min_time)


# Create your models here.
class Sms(models.Model):
    id = models.AutoField(primary_key=True)
    phone_number = models.CharField(max_length=12)
    sms_body = models.CharField(max_length=500)
    created_by = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    valid_sms = SmsManager()

    class Meta:
        ordering = ['-created_at', ]

    def __str__(self):
        return self.sms_body
