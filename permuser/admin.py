from django.contrib import admin
from .models import *


# Register your models here.

admin.site.register(UserPermission)
admin.site.register(EmployeeModel)
admin.site.register(Petitioner)
admin.site.register(Respondent)
admin.site.register(Act)
admin.site.register(Advocate)