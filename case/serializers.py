from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import *
from permuser.serializers import PetitionerSerializer,RespondentSerializer,ActSerializer,AdvocateSerializer

class IADetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=IADetails
        fields='__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields='__all__'

class ObjectionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Objection
        fields='__all__'

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model=History
        fields='__all__'

class DocumentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=DocumentDetails
        fields='__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Notification
        fields='__all__'

class CaseSerializer(serializers.ModelSerializer):
    petitioner=serializers.SerializerMethodField('get_petitioner')
    respondent=serializers.SerializerMethodField('get_respondent')
    act=serializers.SerializerMethodField('get_act')
    advocate=serializers.SerializerMethodField('get_advocate')
    ia=serializers.SerializerMethodField('get_ia')
    history=serializers.SerializerMethodField('get_history')
    order=serializers.SerializerMethodField('get_order')
    objection=serializers.SerializerMethodField('get_objection')
    document=serializers.SerializerMethodField('get_document')
    class Meta:
        model=Case
        fields=["id","cnr_number", "case_type","filling_number","registration_number","petitioner","respondent","act","advocate","ia","history","order","objection","document","case_status"]

    def get_petitioner(self,instance):
        return PetitionerSerializer(instance.petitioner,many=True).data

    def get_respondent(self,instance):
        return RespondentSerializer(instance.respondent,many=True).data

    def get_act(self,instance):
        return ActSerializer(instance.act,many=True).data
    
    def get_advocate(self,instance):
        return AdvocateSerializer(instance.advocate,many=True).data

    def get_ia(self,instance):
        return IADetailsSerializer(instance.ia,many=True).data

    def get_history(self,instance):
        return HistorySerializer(instance.history,many=True).data

    def get_order(self,instance):
        return OrderSerializer(instance.order,many=True).data

    def get_objection(self,instance):
        return ObjectionSerializer(instance.objection,many=True).data

    def get_document(self,instance):
        return DocumentDetailsSerializer(instance.document,many=True).data



class TrackCasesSerializer(serializers.ModelSerializer):
    class Meta:
        model=TrackCases
        fields='__all__'