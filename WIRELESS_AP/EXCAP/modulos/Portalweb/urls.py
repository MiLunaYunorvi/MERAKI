from .views import formulario
from django.urls import path

urlpatterns = [
    #path('',index,name='index'),
    path('',formulario, name='formulario'),
]
