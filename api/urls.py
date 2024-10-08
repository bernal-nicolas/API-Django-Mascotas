from django.urls import path,include
from rest_framework import routers
from api import views

router= routers.DefaultRouter()
router.register(r'mascotas',views.MascotaViewSet)
router.register(r'registros-base', views.RegistrosBaseViewSet)

urlpatterns=[
    path('',include(router.urls)),
    path('verificar-peso/<int:mascota_id>/', views.verificar_peso, name='verificar_peso'),
]