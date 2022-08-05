from django.db import models
import choice
from permuser.models import *

from django.contrib.auth import get_user_model
Users=get_user_model()

class Petition(models.Model):
    case_type=models.CharField(null=True,blank=True, max_length=500,choices=choice.CASE_TYPE,default="")
    case_category=models.CharField(null=True,blank=True, max_length=500,choices=choice.CASE_CATEGORY,default="")
    special_category=models.CharField(null=True,blank=True, max_length=50,default="")
    court=models.CharField(null=True,blank=True, max_length=50, choices=choice.COURT)
    state=models.CharField(max_length=50, null=True,blank=True)
    district=models.CharField(max_length=50, null=True,blank=True)

class Petitioner(models.Model):
    petition=models.ForeignKey(to=Petition,null=True,blank=True,default="",on_delete=models.CASCADE,related_name='petition_petitioner')
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

class Respondent(models.Model):
    petition=models.ForeignKey(to=Petition,null=True,blank=True,default="",on_delete=models.CASCADE,related_name='petition_respondent')
    respondent_name = models.CharField(null=True,blank=True, max_length=50)
    respondent_relation = models.CharField(null=True,blank=True, max_length=50)
    respondent_father = models.CharField(null=True,blank=True, max_length=50)
    respondent_gender = models.CharField(null=True,blank=True, max_length=50)
    respondent_address = models.TextField(null=True,blank=True, max_length= 200)
    respondent_country = models.CharField(null=True,blank=True, max_length=50)
    petitioner_city = models.CharField(null=True,blank=True, max_length=50)
    petitioner_email = models.CharField(null=True,blank=True, max_length=50)


class Act(models.Model):
    petition=models.ForeignKey(to=Petition,null=True,blank=True,default="",on_delete=models.CASCADE,related_name='petition_act')
    act_title=models.CharField(null=True,blank=True, max_length=150)
    act_rule=models.CharField(null=True,blank=True, max_length=150)
    section=models.CharField(null=True,blank=True, max_length=450)
    rule_no=models.IntegerField(null=True,blank=True)
    act_belong_to=models.CharField(null=True,blank=True, max_length=50,choices=choice.ACT_BELONG_TO)