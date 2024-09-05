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
    
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def verificar_peso(request, mascota_id):
    try:
        mascota = Mascota.objects.get(id=mascota_id)
        registro = RegistrosBase.objects.get(raza=mascota.raza, genero=mascota.genero)

        if mascota.peso < registro.peso_minimo:
            resultado = "Inferior"
        elif mascota.peso > registro.peso_maximo:
            resultado = "Superior"
        else:
            resultado = "Ideal"

        response = {
            "peso": resultado,
            "peso_minimo": str(registro.peso_minimo),
            "peso_maximo": str(registro.peso_maximo),
            "peso_actual": str(mascota.peso)
        }

        return Response(response, status=status.HTTP_200_OK)
    except Mascota.DoesNotExist:
        return Response({"error": "Mascota no encontrada"}, status=status.HTTP_404_NOT_FOUND)
    except RegistrosBase.DoesNotExist:
        return Response({"error": "Registro Base no encontrado para la raza y género de la mascota"}, status=status.HTTP_404_NOT_FOUND)