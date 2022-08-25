from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


# Register your models here.

admin.site.register(TabPermission)
# admin.site.register(EmployeeModel)
admin.site.register(CustomUser)

class PetitionerAdmin(admin.ModelAdmin):
    list_display=['id','petitioner_name','petitioner_age','petitioner_state']
admin.site.register(Petitioner,PetitionerAdmin)

class RespondentAdmin(admin.ModelAdmin):
    list_display=['id','respondent_name','respondent_relation','respondent_address']
admin.site.register(Respondent,RespondentAdmin)

admin.site.register(Act)
admin.site.register(Advocate)