from django.db import models
from petitionFiling.models import *
from permuser.models import * 

from django.contrib.auth import get_user_model
Users=get_user_model()

class IADetails(models.Model):
    ia_number=models.CharField(null=True,blank=True, max_length=50)
    party=models.ForeignKey(to=Users,null=True,blank=True,default="",on_delete=models.CASCADE)
    filing_date=models.DateField(null=True,blank=True,default=0)
    next_date=models.DateField(null=True,blank=True,default=0)
    ia_status=models.CharField(null=True,blank=True, max_length=50,choices=choice.IA_STATUS,default="")

    def __str__(self):
        return "%s" %(self.ia_number)

class Order(models.Model): 
    # id=order no (for now)
    judge=models.ForeignKey(to=Judge,null=True,blank=True,default="",on_delete=models.CASCADE)
    order_date=models.DateField(null=True,blank=True,default=0)

    def __str__(self):
        return "%s %s" %(self.id, self.order_date)


class Objection(models.Model):
    scrutiny_date=models.DateField(null=True,blank=True,default=0)
    objection=models.CharField(max_length=500, null=True,blank=True)
    compliance_date=models.DateField(null=True,blank=True,default=0)
    reciept_date=models.DateField(null=True,blank=True,default=0)

    def __str__(self):
        return "%s" %(self.objection)


class DocumentDetails(models.Model):
    document_no=models.IntegerField(null=True,blank=True,default=0)
    recieving_date=models.DateField(null=True,blank=True,default=0)
    filed_by=models.ForeignKey(to=Users,null=True,blank=True,default="",on_delete=models.CASCADE)
    advocate=models.ForeignKey(to=Advocate,null=True,blank=True,default="",on_delete=models.CASCADE)
    document=models.FileField(upload_to="document/",null=True, blank=True)
    document_type=models.CharField(max_length=50, null=True,blank=True)

    def __str__(self):
        return "%s %s" %(self.document_no, self.document_type)

class History(models.Model):
    judge=models.CharField(null=True,blank=True, max_length=50,default="")
    hearing_date=models.DateField(null=True,blank=True,default=0)
    purpose_of_hearing=models.CharField(null=True,blank=True, max_length=50,choices=choice.PURPOSE_OF_HEARING,default="")

    def __str__(self):
        return "%s" %(self.judge)


class Case(models.Model):
    cnr_number=models.CharField(max_length=20, unique=True, null=True)
    case_type=models.CharField(max_length=50, null=True,blank=True,choices=choice.CASE_TYPE)
    filling_number=models.CharField(max_length=20, unique=True, null=True)
    registration_number=models.IntegerField(null=True)

    court=models.CharField(null=True,blank=True, max_length=50, choices=choice.COURT)
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

    petitioner=models.ManyToManyField(Petitioner,null=True,blank=True,related_name='case_petitioner')
    respondent=models.ManyToManyField(Respondent,null=True,blank=True,related_name='case_respondent')
    advocate=models.ManyToManyField(Advocate,null=True,blank=True,related_name='case_advocate')
    act=models.ManyToManyField(Act,null=True,blank=True,related_name='case_act')

    ia=models.ManyToManyField(IADetails,null=True,blank=True,default="",related_name='ia_details')
    history=models.ManyToManyField(History,null=True,blank=True,default="",related_name='case_history')
    order=models.ManyToManyField(Order,null=True,blank=True,default="",related_name='case_order')
    objection=models.ManyToManyField(Objection,null=True,blank=True,default="",related_name='case_objection')
    document=models.ManyToManyField(DocumentDetails,null=True,blank=True,default="",related_name='case_document')
    person_involved=models.ManyToManyField(PersonInvolved,null=True,blank=True,default="",related_name='person_involved')
    ugc_executive=models.ManyToManyField(UGCExecutive,null=True,blank=True,default="",related_name='ugc_executive')


    def petitioners(self):
        return ", ".join([str(p) for p in self.petitioner.all()])

    def respondents(self):
        return ", ".join([str(p) for p in self.respondent.all()])

    def acts(self):
        return ", ".join([str(p) for p in self.act.all()])

class Notification(models.Model):
    case=models.ForeignKey(to=Case,null=True,blank=True,default="",related_name='case_notifications', on_delete=models.CASCADE)
    case_description=models.CharField(max_length=500, null=True,blank=True)
    notification_date=models.DateField(null=True,blank=True,default=None) 
    action_date=models.DateField(null=True,blank=True,default=None) 
    is_notification_recieved=models.BooleanField(null=False,blank=True,default=False)
    notify_to=models.ManyToManyField(Users,null=True,blank=True,default="",related_name='action_notify_to')
    notify_type=models.CharField(max_length=150, null=True,blank=True,choices=choice.NOTIFY_TYPE)
    action_location=models.CharField(max_length=150, null=True,blank=True)

    def __str__(self):
        return "%s" %(self.notify_type)

class TrackCases(models.Model):
    action_status= models.CharField(blank=True, choices=choice.TRACK_TYPE, max_length=150, null=True)
    action_description=models.CharField(max_length=250, null=True,blank=True)
    action_date=models.DateField(null=True,blank=True,default=None) 
    action_taken_by=models.ForeignKey(to=Users,null=True,blank=True,related_name='action_taken_by',on_delete=models.CASCADE)
    case=models.ForeignKey(Case,null=True,blank=True,default="",related_name='case_track',on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" %(self.action_status,self.action_taken_by)