from django.db import models
from django.utils import timezone


# Create your models here.
class Sms(models.Model):
    id = models.AutoField(primary_key=True)
    phone_number = models.CharField(max_length=12)
    sms_body = models.CharField(max_length=500)
    created_by = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at', ]

    def __str__(self):
        return self.sms_body
