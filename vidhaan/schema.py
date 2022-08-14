import graphene
from graphene_django import DjangoObjectType
from case.models import *

class CaseType(DjangoObjectType):
    class Meta:
        model = Case
        exclude_fields = ('id','case_type', 'history')

class Query(graphene.ObjectType):
    cases = graphene.List(CaseType)


schema = graphene.Schema(query=Query)