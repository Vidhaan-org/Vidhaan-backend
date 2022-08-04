from django.db import models
from petitionFiling.models import *
from history.models import *    

class Case(models.Model):
    cnr_number=models.IntegerField(unique=True, null=False)
    case_type=models.CharField(max_length=50, null=True)
    filling_number=models.IntegerField(null=False)
    registration_number=models.IntegerField(null=False)
    registration_number=models.DateField(null=True)
    case_status=models.ForeignKey(to=CaseStatus,null=True,blank=True,default="")
    petitioner=models.ManyToManyField(Petitioner,null=True,blank=True)
    respondent=models.ManyToManyField(Respondent,null=True,blank=True)
    advocate=models.ManyToManyField(Advocate,null=True,blank=True)
    act=models.ManyToManyField(Act,null=True,blank=True)
    ia=models.ForeignKey(to=IADetails,null=True,blank=True,default="")
    history=models.ForeignKey(to=History,null=True,blank=True,default="")
    order=models.ForeignKey(to=Order,null=True,blank=True,default="")
    objection=models.ForeignKey(to=Objection,null=True,blank=True,default="")
    document=models.ForeignKey(to=DocumentDetails,null=True,blank=True,default="")



