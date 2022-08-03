from rest_framework import serializers
from .models import *


class CaseDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=CaseDetails
        fields='__all__'