from django.db import models
import choice

##rough
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
class UserPermission(models.Model):
    name=models.CharField(max_length=100,unique=True)
    can_edit=models.BooleanField(default=False)
    can_upload=models.BooleanField(default=False)

    def __str__(self):
        return "%s" %(self.name)

class EmployeeModel(models.Model):
    organization_permission=models.ForeignKey(to=UserPermission, on_delete=models.CASCADE,null=True,blank=True,related_name='employee_permission')
    employee_name=models.TextField(max_length=50,null=True,blank=True)
    employee_email=models.CharField(max_length=200,unique=True)
    employee_mobile=models.CharField(max_length=200,unique=True)
    employee_password=models.CharField(max_length=200,unique=True)
    permissions=models.ManyToManyField(to=UserPermission,related_name='user_permission',blank=True)

    def __str__(self):
        return "%s" %(self.employee_name)

class Advocate(models.Model):
    advocate_name = models.CharField(null=True,blank=True, max_length=50)
    advocate_number = models.IntegerField(null=True,blank=True)
    advocate_year = models.IntegerField(null=True,blank=True)
    advocate_mobile = models.IntegerField(null=True,blank=True)
    advocate_email_id = models.CharField(null=True,blank=True, max_length=50)
    advocate_type=models.CharField(null=True,blank=True, max_length=50,choices=choice.ADVOCATE_TYPE)

    def __str__(self):
        return "%s" %(self.advocate_name)

class Judge(models.Model):
    judge_name = models.CharField(null=True,blank=True, max_length=50)
    judge_number = models.IntegerField(null=True,blank=True)
    judge_year = models.IntegerField(null=True,blank=True)
    judge_mobile = models.IntegerField(null=True,blank=True)
    judge_email_id = models.CharField(null=True,blank=True, max_length=50)

    def __str__(self):
        return "%s" %(self.judge_name)

class Act(models.Model):
    act_title=models.CharField(null=True,blank=True, max_length=150)
    act_rule=models.CharField(null=True,blank=True, max_length=150)
    section=models.CharField(null=True,blank=True, max_length=450)
    rule_no=models.IntegerField(null=True,blank=True)
    act_belong_to=models.CharField(null=True,blank=True, max_length=50,choices=choice.ACT_BELONG_TO)

    def __str__(self):
        return "%s" %(self.section)


class Petitioner(models.Model):
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

    def __str__(self):
        return "%s" %(self.petitioner_name)


class Respondent(models.Model):
    respondent_name = models.CharField(null=True,blank=True, max_length=50)
    respondent_relation = models.CharField(null=True,blank=True, max_length=50)
    respondent_father = models.CharField(null=True,blank=True, max_length=50)
    respondent_gender = models.CharField(null=True,blank=True, max_length=50)
    respondent_address = models.TextField(null=True,blank=True, max_length= 200)
    respondent_country = models.CharField(null=True,blank=True, max_length=50)
    respondent_city = models.CharField(null=True,blank=True, max_length=50)
    respondent_email = models.CharField(null=True,blank=True, max_length=50)

    def __str__(self):
        return "%s" %(self.respondent_name)



class PersonInvolved(models.Model):
    person_name = models.CharField(null=True,blank=True, max_length=50)
    person_mobile = models.IntegerField(null=True,blank=True)
    person_email = models.CharField(null=True,blank=True, max_length=50)
    person_age = models.CharField(null=True,blank=True, max_length=50)
    person_address = models.CharField(null=True,blank=True, max_length=200)
    person_state = models.CharField(null=True,blank=True, max_length=50)
    person_city = models.CharField(null=True,blank=True, max_length=50)
    person_pin = models.IntegerField(null=True,blank=True)
    
    def __str__(self):
        return "%s" %(self.person_name)