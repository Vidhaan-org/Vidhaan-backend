from django.urls import path

from .views import *
namespace=['case']

urlpatterns=[
    path('details/',CaseDetail.as_view())
]