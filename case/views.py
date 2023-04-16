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
from case.petitionAcceptance import petition_acceptance_metric
from datetime import date

class CaseDetail(GenericAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class=CaseSerializer

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
            # account_sid = os.environ['TWILIO_ACCOUNT_SID']
            # auth_token = os.environ['TWILIO_AUTH_TOKEN']
            # client = Client(account_sid, auth_token)
            # +19786629400
            # message = client.messages \
            #     .create(
            #         body="There is an update in your. VIDHAAN SIH!",
            #         from_='+19786629400',
            #         to='+919179322789'
            #         )

            return Response({
                "status_code": 200,
                "data": serializer.data
            })
        else: 
            return Response({
                "status_code": 400,
                "data": serializer.errors
            })
    def get(self,request):
        cases=Case.objects.all()
        id=request.query_params.get('id', None)
        try:
            if id:
                case=cases.get(id=id)
                serializer=CaseSerializer(case)
                return Response({
                    "status_code": 200,
                    "data": serializer.data
                })
            else:  
                serializer=CaseSerializer(cases,many=True)
                return Response({
                    "status_code": 200,
                    "data": serializer.data
                })
        except ObjectDoesNotExist:
            print(CaseSerializer(cases))  
            return Response({
                "status_code": 400,
                "data": "No Case exist with this id exist!!"
            })
        
            
class CaseList(ListAPIView):
    # permission_classes = [IsAuthenticated]

    serializer_class=CaseSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['cnr_number', 'registration_number', 'ia__filing_date', 'ia__ia_status' , 'court','petitioner__petitioner_name','respondent__respondent_name','person_involved__person_name','case_status','user'] 
    ordering_fields = ['cnr_number']
    search_fields = ['cnr_number', 'registration_number']


    def get_queryset(self):
        queryset=Case.objects.all()
        query=self.request.query_params.get('query')
        if query is not None:  
            return queryset.filter(id__iexact=query) or queryset.filter(case_status__icontains=query) or  queryset.filter(petitioner__petitioner_name__icontains=query) or queryset.filter(respondent__respondent_name__icontains=query)
        else: 
            return queryset

class CaseNotification(ListAPIView): 
    permission_classes = [IsAuthenticated]
    serializer_class=NotificationSerializer
    def get(self,request,id=None):
        try:
            notification=Notification.objects.all()
            serializer=NotificationSerializer(notification, many=True)
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
        serializer=NotificationSerializer(data=request.data)
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

class OptionList(ListAPIView):
    def get(self,request):
        court_list=[]
        act_list=[]
        advocate_list=[]
        case_type_list=[]
        petiton_type_list=[]
        case_category_list=[]
        case_status_list=[]
        special_category_list=[]
        notify_type_list=[]
        track_type_list=[]
        purpose_hearing_list=[]
        ia_details_list=[]

        for court in choice.COURT:
            court_caps, court_title=court
            court_list.append(court_title)
        
        for act in choice.ACT_BELONG_TO:
            act_caps, act_title=act
            act_list.append(act_title)
        
        for advocate in choice.ADVOCATE_TYPE:
            advocate_caps, advocate_title=advocate
            advocate_list.append(advocate_title)

        for case_type in choice.CASE_TYPE:
            case_type_caps, case_type_title=case_type
            case_type_list.append(case_type_title)
        
        for petiton_type in choice.PETITION_TYPE:
            petiton_type_caps, petiton_type_title=petiton_type
            petiton_type_list.append(petiton_type_title)

        for case_category in choice.CASE_CATEGORY:
            case_category_caps, case_category_title=case_category
            case_category_list.append(case_category_title)
        
        for case_status in choice.CASE_STATUS:
            case_status_caps, case_status_title=case_status
            case_status_list.append(case_status_title)
        
        for special_category in choice.SPECIAL_CATEGORY:
            special_category_caps, special_category_title=special_category
            special_category_list.append(special_category_title)

        for notify_type in choice.NOTIFY_TYPE:
            notify_type_caps, notify_type_title=notify_type
            notify_type_list.append(notify_type_title)
        
        for track_type in choice.TRACK_TYPE:
            track_type_caps, track_type_title=track_type
            track_type_list.append(track_type_title)

        for purpose_hearing in choice.PURPOSE_OF_HEARING:
            purpose_hearing_caps, purpose_hearing_title=purpose_hearing
            purpose_hearing_list.append(purpose_hearing_title)

        for ia_details in choice.IA_STATUS:
            ia_details_caps, ia_details_title=ia_details
            ia_details_list.append(ia_details_title)

        return Response({
            "status_code": 200,
            "data": {
                "Court": court_list,
                "Act Belong to": act_list,
                "Advocate Type": advocate_list,
                "Case Type": case_type_list,
                "Petition Type": petiton_type_list,
                "Case Category": case_category_list,
                "Case Status": case_status_list,
                "Special Category": special_category_list,
                "Notify Type": notify_type_list,
                "Track Type": track_type_list,
                "Purpose of Hearing": purpose_hearing_list,
                "IA Status": ia_details_list

            }
        }) 


class TrackCasesList(ListAPIView): 
    permission_classes = [IsAuthenticated]
    serializer_class=TrackCasesSerializer

    def get(self,request, id=None):
        try:
            track_cases=TrackCases.objects.all()
            serializer=TrackCasesSerializer(track_cases, many=True)
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
        serializer=TrackCasesSerializer(data=request.data)
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


class PetitionAcceptance(APIView):
    def post(self,request):
        text=request.data['text']
        acceptance_bool, acceptance_pred=petition_acceptance_metric(text_inp=[text])
        
        return Response({
            "status_code": 200,
            "data": {
                "bool": str(acceptance_bool)[1],
                "pred": str(acceptance_pred)[1:-1]
            }
        })

class DateMonitoring(ListAPIView): 
    permission_classes = [IsAuthenticated]
    serializer_class=NotificationSerializer
    def get(self,request, id=None):
        caseNumber = self.request.query_params.get('case')
        if caseNumber is not None:
            print("not non")
            try:
                notification=Notification.objects.filter(action_date__gte=date.today(), case__cnr_number=caseNumber)
                serializer=NotificationSerializer(notification, many=True)
                return Response({
                    "status_code": 200,
                    "data": serializer.data
                })  
            except ObjectDoesNotExist:
                return Response({
                    "status_code": 400,
                    "data": serializer.errors
                })
        else:
            print("is non")
            try:
                notification=Notification.objects.filter(action_date__gte=date.today())
                serializer=NotificationSerializer(notification, many=True)
                return Response({
                    "status_code": 200,
                    "data": serializer.data
                })
            except ObjectDoesNotExist:
                    return Response({
                        "status_code": 400,
                        "data": serializer.errors
                    })

class advocateSuggestor(APIView):

    def advocate_suggestor(sp,exp=50,fee=35,age=40,avg_resolvetime=69,activecases=45):
        import pandas as pd
        import numpy as np
        df = pd.read_csv('case/dataset_advocate_performance (1).csv',index_col=False)
        del df['Unnamed: 0'],df['id']
        df['experience (yrs)'] = df['experience (yrs)'].astype(int)
        df['active cases'] = df['active cases'].astype(int)
        types_of_cases = ["Arbitration Petition","Civil (Appeal) Petition","Contempt Petition (Civil)","Contempt Petition (Criminal)","Criminal Appeal Petition","Election Petition","Original Suit","Petition for Special Leave to Appeal","Transferred Case Petition","Writ Petition"]

        for i in range(len(types_of_cases)):
            print(f"{i+1} for {types_of_cases[i]}")

        d = df[df['speciality']==types_of_cases[sp-1]]
        actual_order=[]
        inp_order = []
        features = ["experience (yrs)","fees","age","avg resolve time (days)","active cases"]
        actual_order = [[exp,"experience (yrs)"],[fee,"fees"],[age,"age"],[avg_resolvetime,"avg resolve time (days)"],[activecases,"active cases"]]

        actual_order = sorted(actual_order,reverse=True)
        order_list = []
        for i in range(len(actual_order)):
            actual_order[i] = str(actual_order[i][1])
            if actual_order[i]== "experience (yrs)":
                order_list.append(False)
            else:
                order_list.append(True)
        d = d.sort_values(by=actual_order,ascending=order_list)
        d = d.reset_index(drop=True)
        print(d.head())
        return d.head(3).to_json(orient='records') 

    def post(self,request):
        #serializer=AdvocateScoreSerializer(data=request.data)
        data = request.data
        if data is not None:
            score = advocateSuggestor.advocate_suggestor(sp=data["sp"])
            return Response({
                "score": score
            })
        else: 
            return Response({
                "status_code": 400,
                "data": serializer.errors
           })
