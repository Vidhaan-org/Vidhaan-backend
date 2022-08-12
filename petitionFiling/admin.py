from django.contrib import admin
from .models import *


class PetitionAdmin(admin.ModelAdmin):
    list_display=['case_type','petitioners','respondents','acts']

admin.site.register(Petition,PetitionAdmin)