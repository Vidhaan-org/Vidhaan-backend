from django.db import models

from permuser.models import * 

from django.contrib.auth import get_user_model
Users=get_user_model()

class IADetails(models.Model):
    ia_number=models.CharField(null=True,blank=True, max_length=50)
    party=models.ForeignKey(to=Users,null=True,blank=True,default="",on_delete=models.CASCADE)
    filing_date=models.DateField(null=True,blank=True,default=0)
    next_date=models.DateField(null=True,blank=True,default=0)
    ia_status=models.CharField(null=True,blank=True, max_length=50,choices=choice.IA_STATUS,default="")

class Order(models.Model): 
    # id=order no (for now)
    judge=models.ForeignKey(to=Judge,null=True,blank=True,default="",on_delete=models.CASCADE)
    order_date=models.DateField(null=True,blank=True,default=0)


class Objection(models.Model):
    scrutiny_date=models.DateField(null=True,blank=True,default=0)
    objection=models.CharField(max_length=500, null=True,blank=True)
    compliance_date=models.DateField(null=True,blank=True,default=0)
    reciept_date=models.DateField(null=True,blank=True,default=0)


class DocumentDetails(models.Model):
    document_no=models.IntegerField(null=True,blank=True,default=0)
    recieving_date=models.DateField(null=True,blank=True,default=0)
    filed_by=models.ForeignKey(to=Users,null=True,blank=True,default="",on_delete=models.CASCADE)
    advocate=models.ForeignKey(to=Advocate,null=True,blank=True,default="",on_delete=models.CASCADE)
    document=models.FileField(upload_to="document/",null=True, blank=True)

class History(models.Model):
    cause_list_type=models.CharField(max_length=50, null=True,blank=True)
    judge=models.ForeignKey(to=Judge,null=True,blank=True,default="",on_delete=models.CASCADE)
    hearing_date=models.DateField(null=True,blank=True,default=0)
    purpose_of_hearing=models.CharField(null=True,blank=True, max_length=50,choices=choice.PURPOSE_OF_HEARING,default="")


class CaseStatus(models.Model):
    stage_of_case=models.CharField(max_length=50, null=True, blank=True)
    coram=models.CharField(max_length=50, null=True, blank=True,default="")
    bench=models.CharField(max_length=50, null=True,blank=True,default="")
    state=models.CharField(max_length=50, null=True,blank=True,default="")
    district=models.CharField(max_length=50, null=True,blank=True,default="")
    judicial=models.CharField(max_length=50, null=True,blank=True,default="")
    causelist_name=models.CharField(max_length=50, null=True,blank=True,default="")

    latest_hearing=models.DateField(null=True,blank=True,default=None)
    decision_date=models.DateField(null=True,blank=True,default=None)
    case_status=models.CharField(max_length=50, null=True, choices=choice.CASE_STATUS)
    next_date=models.DateField(null=True,blank=True,default=None) 


class Case(models.Model):
    cnr_number=models.IntegerField(unique=True, null=True)
    case_type=models.CharField(max_length=50, null=True,blank=True,choices=choice.CASE_TYPE)
    
    filling_number=models.IntegerField(null=True)
    registration_number=models.IntegerField(null=True)

    petitioner=models.ManyToManyField(Petitioner,null=True,blank=True,related_name='case_petitioner')
    respondent=models.ManyToManyField(Respondent,null=True,blank=True,related_name='case_respondent')
    advocate=models.ManyToManyField(Advocate,null=True,blank=True,related_name='case_advocate')
    act=models.ManyToManyField(Act,null=True,blank=True,related_name='case_act')

    ia=models.ManyToManyField(IADetails,null=True,blank=True,default="",related_name='ia_details')
    history=models.ManyToManyField(History,null=True,blank=True,default="",related_name='case_history')
    order=models.ManyToManyField(Order,null=True,blank=True,default="",related_name='case_order')
    objection=models.ManyToManyField(Objection,null=True,blank=True,default="",related_name='case_objection')
    document=models.ManyToManyField(DocumentDetails,null=True,blank=True,default="",related_name='case_document')


class Notification(models.Model):
    case=models.ManyToManyField(Case,null=True,blank=True,default="",related_name='case_notifications')
    case_title=models.CharField(max_length=250, null=True,blank=True)
    case_description=models.CharField(max_length=500, null=True,blank=True)
    notification_date=models.DateField(null=True,blank=True,default=None) 
    action_date=models.DateField(null=True,blank=True,default=None) 
    is_notification_recieved=models.BooleanField(null=False,blank=True,default=False)

