from rest_framework import serializers
from .models import *


class PetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Petition
<<<<<<< HEAD
        fields='__all__'
=======
        fields='__all__'
>>>>>>> rahul
