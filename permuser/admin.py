from django.contrib import admin
from .models import UserPermission,OrganizationModel,EmployeeModel


# Register your models here.

admin.site.register(UserPermission)
admin.site.register(OrganizationModel)
admin.site.register(EmployeeModel)