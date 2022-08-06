from rest_framework import serializers
from .models import *


class PetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Petition
        fields='__all__'
