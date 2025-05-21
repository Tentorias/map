from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Monta todas as URLs da app “relatorios” sob o namespace 'relatorios'
    path('', include(('relatorios.urls', 'relatorios'), namespace='relatorios')),
]
