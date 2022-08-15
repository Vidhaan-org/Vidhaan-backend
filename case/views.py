from email import message
from typing import List
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import *
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from django.core.mail import send_mail
import os
from twilio.rest import Client

class CaseDetail(GenericAPIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        serializer=CaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            #sending mail
            # case_number = request.POST['cnr_number']
            send_mail(
                'Case Added', #+ case_number,
                'New case added',
                'vidhaan.inbox@gmail.com',
                ['suryansh.1191@gmail.com', 'rahulkesharwani353@gmail.com', 'sonaljain067@gmail.com', 'dewansh.dt@gmail.com', 'emailanubhavagrawal@gmail.com', 'singh.20atulya@gmail.com']
            )

            # seding phone 
            account_sid = os.environ['TWILIO_ACCOUNT_SID']
            auth_token = os.environ['TWILIO_AUTH_TOKEN']
            client = Client(account_sid, auth_token)
            # +19786629400
            message = client.messages \
                .create(
                    body="There is an update in your. VIDHAAN SIH!",
                    from_='+19786629400',
                    to='+919179322789'
                    )

            return Response({
                "status_code": 200,
                "data": serializer.data
            })
        else: 
            return Response({
                "status_code": 400,
                "data": serializer.errors
            })
    def get(self,request,id=None):
        search_query = self.request.query_params.get('search_query') or None
        filter_query=self.request.query_params.get('filter_query') or None

        if not id:
            try:
                case=Case.objects.get(id=id)
                serializer=CaseSerializer(case)
                return Response({
                    "status_code": 200,
                    "data": serializer.data
                })
            except ObjectDoesNotExist:
                return Response({
                    "status_code": 400,
                    "data": serializer.errors
                })
        # elif search_query :
        #     queryset = queryset.filter(purchaser__username=search_query)
        #     return queryset
        elif filter_query: 
            queryset = queryset.filter(purchaser__username=search_query)
            return queryset
        else: 
            try:
                cases=Case.objects.all()
                serializer=CaseSerializer(cases,many=True)
                return Response({
                    "status_code": 200,
                    "data": serializer.data
                })
            except ObjectDoesNotExist:
                return Response({
                    "status_code": 400,
                    "data": serializer.errors
                })
        
            
class CaseList(ListAPIView):
    permission_classes = [IsAuthenticated]

    #seding phone 
    # account_sid = os.environ['TWILIO_ACCOUNT_SID']
    # auth_token = os.environ['TWILIO_AUTH_TOKEN']
    # client = Client(account_sid, auth_token)
    # # +19786629400
    # message = client.messages \
    #         .create(
    #              body="There is an update in your. VIDHAAN SIH!",
    #              from_='+19786629400',
    #              to=['+919179322789']
    #             )

    # send_mail(
    #             'Case Update',
    #             'There is new update on the case',
    #             'vidhaan.inbox@gmail.com',
    #             ['suryansh.1191@gmail.com', 'rahulkesharwani353@gmail.com', 'sonaljain067@gmail.com', 'dewansh.dt@gmail.com', 'emailanubhavagrawal@gmail.com']
    #         ) 
    serializer_class=CaseSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['cnr_number', 'registration_number']
    ordering_fields = ['cnr_number']
    search_fields = ['cnr_number', 'registration_number']



    def get_queryset(self):
        queryset=Case.objects.all()
        query=self.request.query_params.get('query')
        if query is not None:  
            return queryset.filter(case_status_details__case_status__icontains=query) or queryset.filter(cnr_number__iexact=query) or queryset.filter(petitioner__petitioner_name__icontains=query) or queryset.filter(respondent__respondent_name__icontains=query) 
        else: 
            return queryset

