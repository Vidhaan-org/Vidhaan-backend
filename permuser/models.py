from django.db import models


class UserPermission(models.Model):
    name=models.CharField(max_length=100,unique=True)
    can_edit=models.BooleanField(default=False)
    can_upload=models.BooleanField(default=False)
    
class OrganizationModel(models.Model):
    organization_name=models.TextField(max_length=50,null=True,blank=True)
    organization_email=models.CharField(max_length=200,unique=True)

class EmployeeModel(models.Model):
    organization_id=models.ForeignKey(to=OrganizationModel, on_delete=models.CASCADE,null=True,blank=True,related_name='employee_id')
    employee_name=models.TextField(max_length=50,null=True,blank=True)
    employee_email=models.CharField(max_length=200,unique=True)
    employee_mobile=models.CharField(max_length=200,unique=True)
    employee_password=models.CharField(max_length=200,unique=True)
    permissions=models.ManyToManyField(to=UserPermission,related_name='user_permission',blank=True)
