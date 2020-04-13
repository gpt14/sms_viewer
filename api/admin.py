from django.contrib import admin
from .models import Sms
# Register your models here.


class SmsAdmin(admin.ModelAdmin):
    ordering = ['-created_at']
    search_fields = ['sms_body']


admin.site.register(Sms, SmsAdmin)