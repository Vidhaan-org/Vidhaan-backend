from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Petition)
admin.site.register(Petitioner)
admin.site.register(Responded)