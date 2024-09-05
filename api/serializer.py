from rest_framework import serializers
from .models import Mascota, RegistrosBase

class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Mascota
        fields='__all__'
        
class RegistrosBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrosBase
        fields = '__all__'