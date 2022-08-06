from rest_framework import serializers
from .models import *


class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Case
        fields='__all__'

    def create(self,**validate_data):
        return Case.objects.create(**validate_data)