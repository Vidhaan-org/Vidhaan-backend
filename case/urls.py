from django.urls import path,re_path


from .views import *
namespace=['case']

urlpatterns=[
    path('details/',CaseDetail.as_view()),
    path('',CaseList.as_view()),
    path('notification/', CaseNotification.as_view()),
    path('option_list/',OptionList.as_view())
]