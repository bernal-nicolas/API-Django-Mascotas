from rest_framework import viewsets
from .models import Mascota, RegistrosBase
from .serializer import MascotaSerializer, RegistrosBaseSerializer

# Create your views here.

class MascotaViewSet(viewsets.ModelViewSet):
    queryset=Mascota.objects.all()
    serializer_class=MascotaSerializer
    
class RegistrosBaseViewSet(viewsets.ModelViewSet):
    queryset = RegistrosBase.objects.all()
    serializer_class = RegistrosBaseSerializer