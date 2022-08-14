from dataclasses import field
import graphene
from graphene_django import DjangoObjectType
from case.models import *

class CaseType(DjangoObjectType):
    class Meta:
        model = Case
        fields = ('id','case_type', 'history','cnr_number',
        'filling_number',
        )

class Query(graphene.ObjectType):
    cases = graphene.List(CaseType)
    def resolve_cases(root, info, **kwargs):
        # Querying a list
        return Case.objects.all()


schema = graphene.Schema(query=Query)