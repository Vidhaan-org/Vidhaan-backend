from django.urls import path

from .views import *
namespace=['permuser']

urlpatterns=[
    path('',SignUp.as_view()),
    path('profile/',Profile.as_view()),

]