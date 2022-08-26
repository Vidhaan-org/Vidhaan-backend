from django.contrib import admin
from .models import *
from import_export.admin import ExportActionMixin

class CaseAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display=['cnr_number','petitioners','respondents','acts']

admin.site.register(Case,CaseAdmin)
admin.site.register(History)
admin.site.register(IADetails)
admin.site.register(Order)
admin.site.register(Objection)
admin.site.register(DocumentDetails)
admin.site.register(Notification)
admin.site.register(TrackCases)

admin.site.register(PersonInvolved)