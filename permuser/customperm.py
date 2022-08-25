from rest_framework.exceptions import AuthenticationFailed, PermissionDenied
from rest_framework.authentication import BaseAuthentication 
from .models import *
from rest_framework.permissions import BasePermission
from django.contrib.auth import get_user_model

Users=get_user_model()

class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        user=request.GET.get('user')
        if user is None: 
            raise AuthenticationFailed({
                "status_code": 200,
                "data": "Enter User!!"
            })
        try: 
            user=Users.objects.get(username=user)
        except Users.DoesNotExist:
            raise AuthenticationFailed({
                "status_code": 404,
                "data": "User doesn't exist!!"
            })
        return (user,{
            "user": user.id
        })


class AdminPermission(BasePermission):
    def has_permission(self,request,view):
        print(request)
        print(request.data)
        user=request.GET.get('user')
        get_user=Users.objects.get(username=user)
        if get_user.is_admin==True:  
            return True
        raise PermissionDenied({
            "status_code": 403,
            "data": "You don't have permission to access this!!"
        })

class LawyerPermission(BasePermission):
    def has_permission(self,request,view):
        print(request)
        print(request.data)
        user=request.GET.get('user')
        get_user=Users.objects.get(username=user)
        if get_user.is_admin==True:  
            return True
        raise PermissionDenied({
            "status_code": 403,
            "data": "You don't have permission to access this!!"
        })

class UGCExecutivePermission(BasePermission):
    def has_permission(self,request,view):
        print(request)
        print(request.data)
        user=request.GET.get('user')
        get_user=Users.objects.get(username=user)
        if get_user.is_admin==True:  
            return True
        raise PermissionDenied({
            "status_code": 403,
            "data": "You don't have permission to access this!!"
        })
