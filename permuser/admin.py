from django.contrib import admin
from .models import UserPermission,EmployeeModel


# Register your models here.

admin.site.register(UserPermission)
admin.site.register(EmployeeModel)