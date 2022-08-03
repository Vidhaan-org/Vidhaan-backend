from rest_framework import serializers
from .models import *


class PetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Petition
        fields='__all__'


class PetitionerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Petitioner
        fields='__all__'


class RespondentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Respondent
        fields='__all__'


class AdvocateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Advocate
        fields='__all__'


class ActSerializer(serializers.ModelSerializer):
    class Meta:
        model=Act
        fields='__all__'