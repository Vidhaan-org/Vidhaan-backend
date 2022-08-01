from django.contrib import admin
from .models import Petition, Petitioner, Responded


# Register your models here.

admin.site.register(Petition)
admin.site.register(Petitioner)
admin.site.register(Responded)