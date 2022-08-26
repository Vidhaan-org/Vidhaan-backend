from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django_filters.rest_framework import *
from rest_framework.permissions import IsAuthenticated

# add get/post for all permuser
# class CaseNotification(APIView): 
#     permission_classes = [IsAuthenticated]
#     def get(self,request,id=None):
#         try:
#             notification=Notification.objects.all()
#             serializer=NotificationSerializer(notification, many=True)
#             return Response({
#                 "status_code": 200,
#                 "data": serializer.data
#             })
#         except ObjectDoesNotExist:
#                 return Response({
#                     "status_code": 400,
#                     "data": serializer.errors
#                 })

#     def post(self,request):
#         serializer=NotificationSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({
#                 "status_code": 200,
#                 "data": serializer.data
#             })
#         else:
#             return Response({
#                 "status_code": 400,
#                 "data": serializer.errors
#             })


# 
class SignUp(APIView): 
    # permission_classes = [IsAuthenticated]
    def get(self,request,id=None):
        try:
            det=CustomUser.objects.all()
            serializer=CustomUserSerializer(det, many=True)
            return Response({
                "status_code": 200,
                "data": serializer.data
            })
        except ObjectDoesNotExist:
                return Response({
                    "status_code": 400,
                    "data": serializer.errors
                })

    def post(self,request):
        serializer=CustomUserPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status_code": 200,
                "data": serializer.data
            })
        else:
            return Response({
                "status_code": 400,
                "data": serializer.errors
            })

class Profile(APIView):
    def get(self,request):
        
        users=CustomUser.objects.all()
        
        return Response(CustomUserSerializer(users,many=True).data)