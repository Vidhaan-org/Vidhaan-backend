from django.contrib import admin
from .models import *


# Register your models here.

admin.site.register(UserPermission)
admin.site.register(EmployeeModel)

class PetitionerAdmin(admin.ModelAdmin):
    list_display=['id','petitioner_name','petitioner_age','petitioner_state']
admin.site.register(Petitioner,PetitionerAdmin)

class RespondentAdmin(admin.ModelAdmin):
    list_display=['id','respondent_name','respondent_relation','respondent_address']
admin.site.register(Respondent,RespondentAdmin)

admin.site.register(Act)
admin.site.register(Advocate)