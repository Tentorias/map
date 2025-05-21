# relatorios/models.py
from django.db import models
from django.conf import settings
from django.contrib.auth.models import (
    AbstractUser,
    Group,
    Permission,
)
from django.utils.translation import gettext_lazy as _

class Usuario(AbstractUser):
    TIPOS = (
        ('ALUNO', 'Aluno'),
        ('PROFESSOR', 'Professor'),
        ('COORDENADOR', 'Coordenador'),
    )
    tipo = models.CharField(max_length=20, choices=TIPOS, default='ALUNO')

    # === SOBREPOSTAÇÃO dos campos M2M ===
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='usuarios_custom',      # <- related_name único
        related_query_name='usuario_custom'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='usuariosperm_custom',  # <- outro related_name
        related_query_name='usuario_perm_custom'
    )

class Atividade(models.Model):
    TIPO_CHOICES = [
        ('ESTAGIO', 'Estágio'),
        ('MONITORIA', 'Monitoria'),
        ('EXTENSAO', 'Extensão'),
    ]
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    titulo = models.CharField(max_length=200)
    data_inicio = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=[('ATIVA', 'Ativa'), ('ENCERRADA', 'Encerrada')]
    )

class Relatorio(models.Model):
    atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE)
    arquivo = models.FileField(upload_to='relatorios/%Y/%m/')
    data_envio = models.DateTimeField(auto_now_add=True)
    validado = models.BooleanField(default=False)
