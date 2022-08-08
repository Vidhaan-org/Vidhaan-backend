from rest_framework import serializers

from permuser.serializers import PetitionerSerializer,RespondentSerializer,ActSerializer
from .models import *


class PetitionSerializer(serializers.ModelSerializer):
    petitioner=serializers.SerializerMethodField('petition_petitioner')
    respondent=serializers.SerializerMethodField('petition_petitioner')
    act=serializers.SerializerMethodField('petition_act')
    class Meta:
        model=Petition
        fields=["case_type","case_category","special_category","court","state","district"]

    def get_petitioner(self,instance):
        try: 
            query=Petitioner.objects.get(user=instance)
        except Petitioner.DoesNotExist: 
            return False
        return PetitionerSerializer(query).data

    def get_respondent(self,instance):
        try: 
            query=Respondent.objects.get(user=instance)
        except Respondent.DoesNotExist: 
            return False
        return RespondentSerializer(query).data

    def get_act(self,instance):
        try: 
            query=Act.objects.get(user=instance)
        except Act.DoesNotExist: 
            return False
        return ActSerializer(query).data

        
