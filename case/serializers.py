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
        fields=["cnr_number", "case_type","filling_number","registration_number","petitioner","respondent","act","advocate","ia","history","order","objection","document"]

    def get_petitioner(self,instance):
        try: 
            query=Petitioner.objects.all()
        except Petitioner.DoesNotExist: 
            return False
        return PetitionerSerializer(query,many=True).data

    def get_respondent(self,instance):
        try: 
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
    
    def get_advocate(self,instance):
        try: 
            query=Advocate.objects.all()
        except Advocate.DoesNotExist: 
            return False
        return AdvocateSerializer(query,many=True).data

    def get_ia(self,instance):
        try: 
            query=IADetails.objects.all()
        except Petitioner.DoesNotExist: 
            return False
        return IADetailsSerializer(query,many=True).data

    def get_history(self,instance):
        try: 
            query=History.objects.all()
        except History.DoesNotExist: 
            return False
        return HistorySerializer(query,many=True).data

    def get_order(self,instance):
        try: 
            query=Order.objects.all()
        except Order.DoesNotExist:  
            return False
        return OrderSerializer(query,many=True).data

    def get_objection(self,instance):
        try: 
            query=Objection.objects.all()
        except Objection.DoesNotExist: 
            return False
        return ObjectionSerializer(query,many=True).data

    def get_document(self,instance):
        try: 
            query=DocumentDetails.objects.all()
        except DocumentDetails.DoesNotExist: 
            return False
        return DocumentDetailsSerializer(query,many=True).data