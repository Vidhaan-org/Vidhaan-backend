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


class CaseDetail(GenericAPIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        serializer=CaseSerializer(data=request.data)
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

