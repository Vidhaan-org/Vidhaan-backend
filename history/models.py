from django.db import models
from case.models import Case
from permuser.models import *
import choice 
from django.contrib.auth import get_user_model
Users=get_user_model()

class IADetails(models.Model):
    ia_number=models.CharField(null=True,blank=True, max_length=50)
    party=models.ForeignKey(to=Users,null=True,blank=True,default="")
    filing_date=models.DateField(null=True,blank=True,default=0)
    next_date=models.DateField(null=True,blank=True,default=0)
    ia_status=models.CharField(null=True,blank=True, max_length=50,choices=choice.IA_STATUS,default="")

class Order(models.Model): 
    # id=order no (for now)
    cnr_no=models.ForeignKey(to=Case,null=True,blank=True,default="")
    judge=models.ForeignKey(to=Judge,null=True,blank=True,default="")
    order_date=models.DateField(null=True,blank=True,default=0)


class Objection(models.Model):
    cnr_no=models.ForeignKey(to=Case,null=True,blank=True,default="")
    scrutiny_date=models.DateField(null=True,blank=True,default=0)
    objection=models.CharField(max_length=500, null=True,blank=True)
    compliance_date=models.DateField(null=True,blank=True,default=0)
    reciept_date=models.DateField(null=True,blank=True,default=0)


class DocumentDetails(models.Model):
    cnr_no=models.ForeignKey(to=Case,null=True,blank=True,default="")
    document_no=models.IntegerField(null=True,blank=True,default=0)
    recieving_date=models.DateField(null=True,blank=True,default=0)
    filed_by=models.ForeignKey(to=Users,null=True,blank=True,default="")
    advocate=models.ForeignKey(to=Advocate,null=True,blank=True,default="")
    document=models.FileField(upload_to="document/",null=True, blank=True)

class History(models.Model):
    cnr_no=models.ForeignKey(to=Case,null=True,blank=True,default="")
    cause_list_type=models.CharField(max_length=50, null=True,blank=True)
    judge=models.ForeignKey(to=Judge,null=True,blank=True,default="")
    hearing_date=models.DateField(null=True,blank=True,default=0)
    purpose_of_hearing=models.CharField(null=True,blank=True, max_length=50,choices=choice.PURPOSE_OF_HEARING,default="")


class CaseStatus(models.Model):
    cnr_no=models.ForeignKey(to=Case,null=True,blank=True,default="")
    stage_of_case=models.CharField(max_length=50, null=False, blank=True)
    coram=models.CharField(max_length=50, null=False, blank=True,default="")
    bench=models.CharField(max_length=50, null=True,blank=True,default="")
    state=models.CharField(max_length=50, null=True,blank=True,default="")
    district=models.CharField(max_length=50, null=True,blank=True,default="")
    judicial=models.CharField(max_length=50, null=True,blank=True,default="")
    causelist_name=models.CharField(max_length=50, null=True,blank=True,default="")

    latest_hearing=models.DateField(null=True,blank=True,default="")
    decision_date=models.DateField(null=True,blank=True,default="")
    case_status=models.CharField(max_length=50, null=False, choices=choice.CASE_STATUS)
    next_date=models.DateField(null=True,blank=True,default="") 
