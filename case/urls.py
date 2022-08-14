from django.urls import path,re_path


from .views import *
namespace=['case']

urlpatterns=[
    path('details/',CaseDetail.as_view()),
    path('',CaseList.as_view()),
]