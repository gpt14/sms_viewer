
from .models import Sms
from rest_framework import serializers


class SmsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sms
        fields = ['phone_number', 'sms_body', 'created_at']
