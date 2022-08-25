from rest_framework import serializers

from case.models import TrackCases
from .models import *

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

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=["id","username","first_name","last_name","user_type","tab_permission"]


class CustomUserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=["name","email_address","username","password","user_type","tab_permission"]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tags
        fields='__all__'