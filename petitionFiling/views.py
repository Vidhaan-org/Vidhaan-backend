from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework.generics import GenericAPIView

class FilePetition(GenericAPIView):
    def post(self,request):
        serializer=PetitionSerializer(data=request.data)
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
    def get(self,reques):
        petition=Petition.objects.all()
        serializer=PetitionSerializer(petition,many=True)
        return Response({
                "status_code": 200,
                "data": serializer.data
        })



