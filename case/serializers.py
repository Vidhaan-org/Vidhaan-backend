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
    petitioner=serializers.SerializerMethodField('case_petitioner')
    respondent=serializers.SerializerMethodField('case_petitioner')
    act=serializers.SerializerMethodField('case_act')
    advocate=serializers.SerializerMethodField('case_advocate')

    ia=serializers.SerializerMethodField('ia_details')
    history=serializers.SerializerMethodField('case_history')
    order=serializers.SerializerMethodField('case_order')
    objection=serializers.SerializerMethodField('case_objection')
    document=serializers.SerializerMethodField('case_document')

    class Meta:
        model=Case
        fields='__all__'

    def create(self,**validate_data):
        return Case.objects.create(**validate_data)

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

    def get_ia(self,instance):
        try: 
            query=IADetails.objects.get(user=instance)
        except Petitioner.DoesNotExist: 
            return False
        return IADetailsSerializer(query).data
    
    def get_history(self,instance):
        try: 
            query=History.objects.get(user=instance)
        except History.DoesNotExist: 
            return False
        return HistorySerializer(query).data

    def get_order(self,instance):
        try: 
            query=Order.objects.get(user=instance)
        except Order.DoesNotExist: 
            return False
        return OrderSerializer(query).data

    def get_objection(self,instance):
        try: 
            query=Objection.objects.get(user=instance)
        except Objection.DoesNotExist: 
            return False
        return ObjectionSerializer(query).data

    def get_document(self,instance):
        try: 
            query=DocumentDetails.objects.get(user=instance)
        except DocumentDetails.DoesNotExist: 
            return False
        return DocumentDetailsSerializer(query).data