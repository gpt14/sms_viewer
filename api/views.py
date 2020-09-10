from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Sms
from .serializers import SmsSerializer
from rest_framework.response import Response
from rest_framework import viewsets


@permission_classes([IsAuthenticated])
class SmsViewSet(viewsets.ModelViewSet):
    serializer_class = SmsSerializer
    queryset = Sms.valid_sms.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['phone_number']

