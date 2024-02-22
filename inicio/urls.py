from django.urls import path
from inicio.views import inicio, crear_cliente, lista

urlpatterns = [
    path('', inicio, name='inicio'),
    path('clientes/', crear_cliente, name= 'crear_cliente'),
    path('registrados/', lista, name= 'lista')



]