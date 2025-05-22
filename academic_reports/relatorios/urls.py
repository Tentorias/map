from django.urls import path
from . import views

app_name = 'relatorios'  

urlpatterns = [
    path('', views.home, name='home'),
    path('atividades/', views.atividades, name='atividades'),
    path('atividades/nova/', views.atividade_nova, name='atividade_nova'),
    path('relatorios/', views.relatorios, name='relatorios'),
    path('relatorios/<int:id>/validar/', views.validar_relatorio, name='validar_relatorio'),
    path('relatorios/<str:tipo>/', views.visualizar_relatorio, name='visualizar_relatorio'),

]
