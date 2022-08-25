from django.db import models
from django.contrib.auth import get_user_model
from permuser.models import *
import choice

Users=get_user_model()

class Petition(models.Model):
    case_type=models.CharField(null=True,blank=True, max_length=500,choices=choice.CASE_TYPE,default="")
    case_category=models.CharField(null=True,blank=True, max_length=500,choices=choice.CASE_CATEGORY,default="")
    special_category=models.CharField(null=True,blank=True, max_length=50,default="")
    court=models.CharField(null=True,blank=True, max_length=50, choices=choice.COURT)
    state=models.CharField(max_length=50, null=True,blank=True)
    district=models.CharField(max_length=50, null=True,blank=True)

    petitioner=models.ManyToManyField(Petitioner,null=True,blank=True,related_name='petition_petitioner')
    respondent=models.ManyToManyField(Respondent,null=True,blank=True,related_name='petition_respondent')
    act=models.ManyToManyField(Act,null=True,blank=True,related_name='petition_act')