from dataclasses import field, fields
from pyexpat import model
import graphene
from graphene_django import DjangoObjectType
from case.models import *
from petitionFiling.models import *
from permuser.models import *

class CaseType(DjangoObjectType):
    class Meta:
        model = Case
        fields = ('id','case_type', 'history','cnr_number',
        'filling_number', 'case_status', 'court', 'petitioner', 'state_of_case','district','judicial','causelist_name','latest_hearing','decision_date','case_status','next_date','state_of_case','district','judicial','causelist_name','latest_hearing','decision_date','case_status','next_date')

class PetitionerType(DjangoObjectType):
    class Meta:
        model = Petitioner
        fields = ('id','petitioner_type', 'petitioner_name')
      
class PetitionsList(DjangoObjectType):
    class Meta:
        model = Petition
        fields = ('id','petition_file_date'
        )

class TrackCaseList(DjangoObjectType):
    class Meta:
        model = TrackCases
        fields = ('action_status','action_date','case_id')
    
class Query(graphene.ObjectType):
    cases = graphene.List(CaseType)


    casesTrackDetails = graphene.List(TrackCaseList)
    petitionFile = graphene.List(PetitionsList)
    petioner = graphene.List(PetitionerType)

        
    def resolve_cases(root, info, **kwargs):
        # Querying a list
        return Case.objects.all()

    def resolve_casesTrackDetails(root, info, **kwargs): 
        # Querying a list
        return TrackCases.objects.all()

    def resolve_petitionFile(root, info, **kwargs):
        # Querying a list
        return Petition.objects.all()

    def resolve_pationer(root, info, **kwargs):
        # Querying a list
        return Petitioner.objects.select_related("case_petitioner").all()


schema = graphene.Schema(query=Query)