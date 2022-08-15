# from dataclasses import field
import graphene
from graphene_django import DjangoObjectType, DjangoListField
from case.models import *
from permuser.models import *

class PetitionerType(DjangoObjectType):
    class Meta:
        model = Petitioner 
        fields = '__all__'
class CaseType(DjangoObjectType):
    class Meta:
        model = Case
        fields = ('id','case_type', 'history','cnr_number',
        'filling_number'
        )

class Query(graphene.ObjectType):
    cases = graphene.List(CaseType)
    petitioner=DjangoListField(PetitionerType) 
    def resolve_cases(root, info, **kwargs):
        # Querying a list
        return Case.objects.all()

    def resolve_petitioner(root,info):
        return Petitioner.objects.all()


schema = graphene.Schema(query=Query)