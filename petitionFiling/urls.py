from django.contrib import admin 
from django.urls import path

from petitionFiling.views import *
namespace=['file_petition']
urlpatterns=[
    path('',FilePetition.as_view()),
    path('add_petitioner/',Petitioner.as_view()),
    path('add_respondent/',Respondent.as_view()),
    path('add_act/',Act.as_view()),
    path('add_advocate/',Advocate.as_view())
]