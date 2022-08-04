from django.db import models
import choice

class UserPermission(models.Model):
    name=models.CharField(max_length=100,unique=True)
    can_edit=models.BooleanField(default=False)
    can_upload=models.BooleanField(default=False)

class EmployeeModel(models.Model):
    organization_permission=models.ForeignKey(to=UserPermission, on_delete=models.CASCADE,null=True,blank=True,related_name='employee_permission')
    employee_name=models.TextField(max_length=50,null=True,blank=True)
    employee_email=models.CharField(max_length=200,unique=True)
    employee_mobile=models.CharField(max_length=200,unique=True)
    employee_password=models.CharField(max_length=200,unique=True)
    permissions=models.ManyToManyField(to=UserPermission,related_name='user_permission',blank=True)

class Advocate(models.Model):
    advocate_name = models.CharField(null=True,blank=True, max_length=50)
    advocate_number = models.IntegerField(null=True,blank=True)
    advocate_year = models.IntegerField(null=True,blank=True)
    advocate_mobile = models.IntegerField(null=True,blank=True)
    advocate_email_id = models.CharField(null=True,blank=True, max_length=50)
    advocate_type=models.CharField(null=True,blank=True, max_length=50,choices=choice.ADVOCATE_TYPE)

class Judge(models.Model):
    advocate_name = models.CharField(null=True,blank=True, max_length=50)
    advocate_number = models.IntegerField(null=True,blank=True)
    advocate_year = models.IntegerField(null=True,blank=True)
    advocate_mobile = models.IntegerField(null=True,blank=True)
    advocate_email_id = models.CharField(null=True,blank=True, max_length=50)
    advocate_type=models.CharField(null=True,blank=True, max_length=50,choices=choice.ADVOCATE_TYPE)
