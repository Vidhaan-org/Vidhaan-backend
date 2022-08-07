from django.db import models
from petitionFiling.models import *
from permuser.models import * 

from django.contrib.auth import get_user_model
Users=get_user_model()

class Case(models.Model):
    cnr_number=models.IntegerField(unique=True, null=True)
    case_type=models.CharField(max_length=50, null=True,blank=True,choices=choice.CASE_TYPE)
    filling_number=models.IntegerField(null=True)
    registration_number=models.IntegerField()


class IADetails(models.Model):
    case=models.ForeignKey(to=Case,null=True,blank=True,default="",on_delete=models.CASCADE,related_name='case_ia_details')
    ia_number=models.CharField(null=True,blank=True, max_length=50)
    party=models.ForeignKey(to=Users,null=True,blank=True,default="",on_delete=models.CASCADE)
    filing_date=models.DateField(null=True,blank=True,default=0)
    next_date=models.DateField(null=True,blank=True,default=0)
    ia_status=models.CharField(null=True,blank=True, max_length=50,choices=choice.IA_STATUS,default="")

class Order(models.Model): 
    # id=order no (for now)
    case=models.ForeignKey(to=Case,null=True,blank=True,default="",on_delete=models.CASCADE,related_name='case_order')
    judge=models.ForeignKey(to=Judge,null=True,blank=True,default="",on_delete=models.CASCADE)
    order_date=models.DateField(null=True,blank=True,default=0)


class Objection(models.Model):
    case=models.ForeignKey(to=Case,null=True,blank=True,default="",on_delete=models.CASCADE,related_name='case_objection')
    scrutiny_date=models.DateField(null=True,blank=True,default=0)
    objection=models.CharField(max_length=500, null=True,blank=True)
    compliance_date=models.DateField(null=True,blank=True,default=0)
    reciept_date=models.DateField(null=True,blank=True,default=0)


class DocumentDetails(models.Model):
    case=models.ForeignKey(to=Case,null=True,blank=True,default="",on_delete=models.CASCADE,related_name='case_document')
    document_no=models.IntegerField(null=True,blank=True,default=0)
    recieving_date=models.DateField(null=True,blank=True,default=0)
    filed_by=models.ForeignKey(to=Users,null=True,blank=True,default="",on_delete=models.CASCADE)
    advocate=models.ForeignKey(to=Advocate,null=True,blank=True,default="",on_delete=models.CASCADE)
    document=models.FileField(upload_to="document/",null=True, blank=True)

class History(models.Model):
    case=models.ForeignKey(to=Case,null=True,blank=True,default="",on_delete=models.CASCADE,related_name='case_history')
    cause_list_type=models.CharField(max_length=50, null=True,blank=True)
    judge=models.ForeignKey(to=Judge,null=True,blank=True,default="",on_delete=models.CASCADE)
    hearing_date=models.DateField(null=True,blank=True,default=0)
    purpose_of_hearing=models.CharField(null=True,blank=True, max_length=50,choices=choice.PURPOSE_OF_HEARING,default="")


class CaseStatus(models.Model):
    case=models.ForeignKey(to=Case,null=True,blank=True,default="",on_delete=models.CASCADE,related_name='case_status')
    stage_of_case=models.CharField(max_length=50, null=True, blank=True)
    coram=models.CharField(max_length=50, null=True, blank=True,default="")
    bench=models.CharField(max_length=50, null=True,blank=True,default="")
    state=models.CharField(max_length=50, null=True,blank=True,default="")
    district=models.CharField(max_length=50, null=True,blank=True,default="")
    judicial=models.CharField(max_length=50, null=True,blank=True,default="")
    causelist_name=models.CharField(max_length=50, null=True,blank=True,default="")

    latest_hearing=models.DateField(null=True,blank=True,default="")
    decision_date=models.DateField(null=True,blank=True,default="")
    case_status=models.CharField(max_length=50, null=True, choices=choice.CASE_STATUS)
    next_date=models.DateField(null=True,blank=True,default="") 


class CasePetitioner(models.Model):
    case=models.ForeignKey(to=Case,default="",on_delete=models.CASCADE,related_name='case_petitioner')
    petitioner_type = models.CharField(null=True,blank=True,choices=choice.PETITION_TYPE,default="",max_length=50)
    petitioner_name = models.CharField(null=True,blank=True, max_length=50)
    petitioner_age = models.CharField(null=True,blank=True, max_length=50)
    petitioner_state = models.CharField(null=True,blank=True, max_length=50)
    petitioner_address = models.CharField(null=True,blank=True, max_length=200)
    petitioner_country = models.CharField(null=True,blank=True, max_length=50)
    petitioner_mobile = models.IntegerField(null=True,blank=True)
    petitioner_department = models.CharField(null=True,blank=True, max_length=50)
    petitioner_city = models.CharField(null=True,blank=True, max_length=50)
    petitioner_email = models.CharField(null=True,blank=True, max_length=50)
    petitioner_pin = models.IntegerField(null=True,blank=True)
    petitioner_district = models.CharField(null=True,blank=True, max_length=50)
    petitioner_total_petition = models.IntegerField(null=True,blank=True)

class CaseRespondent(models.Model):
    case=models.ForeignKey(to=Case,null=True,blank=True,default="",on_delete=models.CASCADE,related_name='case_respondent')
    respondent_name = models.CharField(null=True,blank=True, max_length=50)
    respondent_relation = models.CharField(null=True,blank=True, max_length=50)
    respondent_father = models.CharField(null=True,blank=True, max_length=50)
    respondent_gender = models.CharField(null=True,blank=True, max_length=50)
    respondent_address = models.TextField(null=True,blank=True, max_length= 200)
    respondent_country = models.CharField(null=True,blank=True, max_length=50)
    petitioner_city = models.CharField(null=True,blank=True, max_length=50)
    petitioner_email = models.CharField(null=True,blank=True, max_length=50)


class CaseAct(models.Model):
    case=models.ForeignKey(to=Case,null=True,blank=True,default="",on_delete=models.CASCADE,related_name='case_act')
    petition=models.ForeignKey(to=Petition,null=True,blank=True,default="",on_delete=models.CASCADE,related_name='case_petitioner')
    act_title=models.CharField(null=True,blank=True, max_length=150)
    act_rule=models.CharField(null=True,blank=True, max_length=150)
    section=models.CharField(null=True,blank=True, max_length=450)
    rule_no=models.IntegerField(null=True,blank=True)
    act_belong_to=models.CharField(null=True,blank=True, max_length=50,choices=choice.ACT_BELONG_TO)


class Notification(models.Model):
    case=models.ForeignKey(to=Case,null=True,blank=True,default="",on_delete=models.CASCADE,related_name='case_notifications')
    title=models.CharField(max_length=250, null=True,blank=True)
    mail_description=models.CharField(max_length=5000, null=True,blank=True)
    web_description=models.CharField(max_length=500, null=True,blank=True)
    is_viewed_in_mail=models.BooleanField(null=True,blank=True,default=False)
    is_viewed_in_web=models.BooleanField(null=True,blank=True,default=False)


