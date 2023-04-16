from rest_framework import serializers

from permuser.serializers import PetitionerSerializer,RespondentSerializer,ActSerializer
from .models import *


class PetitionSerializer(serializers.ModelSerializer):
     
    petitioner=serializers.SerializerMethodField('get_petitioner')
    respondent=serializers.SerializerMethodField('get_respondent')
    act=serializers.SerializerMethodField('get_act')
    class Meta:
        model=Petition
        fields='__all__'
        fields=["case_type","case_category","special_category","court","state","district","petitioner","respondent","act"]

    def get_petitioner(self,instance):
        try: 
            query=Petitioner.objects.all() 
        except Petitioner.DoesNotExist: 
            return False
        return PetitionerSerializer(query,many=True).data

    def get_respondent(self,instance):
        try: 
            print(instance)
            query=Respondent.objects.all()
        except Respondent.DoesNotExist: 
            return False
        return RespondentSerializer(query,many=True).data

    def get_act(self,instance):
        try: 
            query=Act.objects.all()
        except Act.DoesNotExist: 
            return False
        return ActSerializer(query,many=True).data
