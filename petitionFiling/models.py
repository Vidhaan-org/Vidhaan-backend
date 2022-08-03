from django.db import models
import choice

class Petition(models.Model):
    case_type=models.CharField(null=True,blank=True, max_length=50,choices=choice.CASE_TYPE,default="")
    case_category=models.CharField(null=True,blank=True, max_length=50,choices=choice.CASE_CATEGORY,default="")
    special_category=models.CharField(null=True,blank=True, max_length=50,default="")
    court=models.CharField(null=True,blank=True, max_length=50, choices=choice.COURT)
    state=models.CharField(max_length=50, null=True,blank=True)
    

class Petitioner(models.Model):
    # link to one/multiple petition
    petition=models.ManyToManyField(Petition,null=True,blank=True)
    petitioner_type = models.CharField(null=True,blank=True, max_length=50,choices=choice.PETITION_TYPE,default="")
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
    # link to one/multiple petition
    petition=models.ManyToManyField(Petition,null=True,blank=True)
    respondent_name = models.CharField(null=True,blank=True, max_length=50)
    respondent_relation = models.CharField(null=True,blank=True, max_length=50)
    respondent_father = models.CharField(null=True,blank=True, max_length=50)
    respondent_gender = models.CharField(null=True,blank=True, max_length=50)
    respondent_address = models.TextField(null=True,blank=True, max_length= 200)
    respondent_country = models.CharField(null=True,blank=True, max_length=50)
    petitioner_city = models.CharField(null=True,blank=True, max_length=50)
    petitioner_email = models.CharField(null=True,blank=True, max_length=50)

class Advocate(models.Model):
    # link to one/multiple cases
    petition=models.ManyToManyField(Petition,null=True,blank=True)
    advocate_name = models.CharField(null=True,blank=True, max_length=50)
    advocate_number = models.IntegerField(null=True,blank=True)
    advocate_year = models.IntegerField(null=True,blank=True)
    advocate_mobile = models.IntegerField(null=True,blank=True)
    advocate_email_id = models.CharField(null=True,blank=True, max_length=50)
    advocate_type=models.CharField(null=True,blank=True, max_length=50,choices=choice.ADVOCATE_TYPE)

class Act(models.Model):
    petition=models.ManyToManyField(Petition,null=True,blank=True)
    act_title=models.CharField(null=True,blank=True, max_length=150)
    central_rule=models.CharField(null=True,blank=True, max_length=150)
    section=models.CharField(null=True,blank=True, max_length=450)
    rule_no=models.IntegerField(null=True,blank=True)
    act_belong_to=models.CharField(null=True,blank=True, max_length=50,choices=choice.ACT_BELONG_TO)

