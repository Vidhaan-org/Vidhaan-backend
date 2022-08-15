from django.contrib import admin
from .models import *


# Register your models here.

admin.site.register(UserPermission)
admin.site.register(EmployeeModel)

class PetitionerAdmin(admin.ModelAdmin):
    list_display=['petitioner_name']
admin.site.register(Petitioner,PetitionerAdmin)
admin.site.register(Respondent)
admin.site.register(Act)
admin.site.register(Advocate)