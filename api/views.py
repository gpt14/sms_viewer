from django.shortcuts import render
from .models import Sms
from .serializers import SmsSerializer
from rest_framework.response import Response
from rest_framework import viewsets


class SmsViewSet(viewsets.ModelViewSet):
    serializer_class = SmsSerializer
    queryset = Sms.objects.all()
