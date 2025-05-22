# relatorios/urls.py
from django.urls import path
from . import views

app_name = 'relatorios'

urlpatterns = [
    path('', views.home, name='home'),

    # Atividades
    path('atividades/', views.atividades, name='atividades'),
    path('atividades/nova/', views.atividade_nova, name='atividade_nova'),

    # Tela geral de relatórios (menu)
    path('relatorios/', views.relatorios, name='relatorios'),

    # Validação pontual de Relatorio já enviado
    path('relatorios/<int:id>/validar/', views.validar_relatorio, name='validar_relatorio'),

    # Envio de novo relatório para um tipo específico
    path('relatorios/<str:tipo>/', views.enviar_relatorio, name='enviar_relatorio'),

    # Listagem de todos os relatórios de um tipo
    path('relatorios/<str:tipo>/listar/', views.listar_relatorios, name='listar_relatorios'),
]
