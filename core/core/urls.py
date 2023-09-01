from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('clientes/', include('clientes.urls')),
    path('servicos/', include('servicos.urls')),
    path('admin/', admin.site.urls),
]
