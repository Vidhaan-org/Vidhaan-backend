from rest_framework import serializers

from permuser.serializers import PetitionerSerializer,RespondentSerializer,ActSerializer
from .models import *

class PetitionSerializer(serializers.ModelSerializer):
    petitioner=serializers.SerializerMethodField('get_petitioner')
    respondent=serializers.SerializerMethodField('get_respondent')
    act=serializers.SerializerMethodField('get_act')
    class Meta:
        model=Petition
        fields=["case_type","case_category","special_category","court","state","district","petitioner","respondent","act"]

    def get_petitioner(self,instance):
        return PetitionerSerializer(instance.petitioner,many=True).data

    def get_respondent(self,instance):
        return RespondentSerializer(instance.respondent,many=True).data

    def get_act(self,instance):
        return ActSerializer(instance.act,many=True).data
        
