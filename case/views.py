from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *
from django.core.exceptions import ObjectDoesNotExist

class CaseDetail(APIView):
    def post(self,request):
        serializer=CaseDetailsSerializer(data=request.data)
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
        if id:
            try:
                case=CaseDetails.objects.get(id=id)
                serializer=CaseDetailsSerializer(case)
                return Response({
                    "status_code": 200,
                    "data": serializer.data
                })
            except ObjectDoesNotExist:
                return Response({
                    "status_code": 400,
                    "data": serializer.errors
                })
        try:
            cases=CaseDetails.objects.all()
            serializer=CaseDetailsSerializer(cases,many=True)
            return Response({
                "status_code": 200,
                "data": serializer.data
            })
        except ObjectDoesNotExist:
            return Response({
                "status_code": 400,
                "data": serializer.errors
            })

