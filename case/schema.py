# from ast import If
# from dataclasses import field, fields
# from pyexpat import model
# import graphene
# from graphene_django import DjangoObjectType
# from case.models import *
# from petitionFiling.models import *
# from permuser.models import *

# class CaseType(DjangoObjectType):
#     class Meta:
#         model = Case
#         fields = '__all__'

# class LawerType(DjangoObjectType):
#     class Meta:
#         model = Advocate
#         fields = ('advocate_name', 'advocate_number')

# class JudgeType(DjangoObjectType):
#     class Meta:
#         model = Judge
#        fields = ('judge_name', 'judge_number')
# class PetitionerType(DjangoObjectType):
#    class Meta:
#        model = Petitioner
#        fields = ('id','petitioner_type', 'petitioner_name')
      
# class PetitionsList(DjangoObjectType):
#    class Meta:
#        model = Petition
#        fields = '__all__'

# class ActType(DjangoObjectType):
#    class Meta:
#       model = Act
#       fields = '__all__'

#class TrackCaseList(DjangoObjectType):
#    class Meta:
#        model = TrackCases
#        fields = ('action_status','action_date','case_id')
    
#class Query(graphene.ObjectType):
#    cases = graphene.List(CaseType)


#    casesTrackDetails = graphene.List(TrackCaseList)
#    petitionFile = graphene.List(PetitionsList)
#    petioner = graphene.List(PetitionerType)
#    lawers = graphene.List(LawerType)
#    judge = graphene.List(JudgeType)
#    act = graphene.List(ActType)

#    @graphene.resolve_only_args
#    def resolve_act(self):
#        if not self:
#            return Act.objects.all() 
#        else:
#            return self.act.all()




#    @graphene.resolve_only_args
#    def resolve_petioner(self):
#        print(self)
#        if not self:
#            return Petitioner.objects.all()
#        else:
#            return self.petioner.all()
    
#    @graphene.resolve_only_args
#    def resolve_judge(self):
#        print(self)
#        if not self:
#            return Judge.objects.all()
#        else:
#            return self.judge.all()
    
#    @graphene.resolve_only_args
#    def resolve_lawer(self):
#        # Querying a list
#        if not self:
#            return Judge.objects.all()
#        else:
#            return self.lawers.all()
        
#    def resolve_cases(root, info, **kwargs):
        # Querying a list
#        return Case.objects.all()

#    def resolve_casesTrackDetails(root, info, **kwargs): 
        # Querying a list
#        return TrackCases.objects.all()

#    def resolve_petitionFile(root, info, **kwargs):
        # Querying a list
#        return Petition.objects.all()

    # def resolve_petioner(root, info, **kwargs):
    #     # Querying a list
    #     return Petitioner.objects.all()


# schema = graphene.Schema(query=Query)
