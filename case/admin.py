from django.contrib import admin
from .models import *

class CaseAdmin(admin.ModelAdmin):
    list_display=['cnr_number','petitioners','respondents','acts']

admin.site.register(Case,CaseAdmin)
admin.site.register(History)
admin.site.register(IADetails)
admin.site.register(Order)
admin.site.register(Objection)
admin.site.register(DocumentDetails)
admin.site.register(CaseStatus)
admin.site.register(Notification)