"""Proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from aplicaciones.principal.views import inicio
from aplicaciones.principal.views import getEventos, eventos, evento_detail, about
from aplicaciones.principal.views import crearEvento
from django.conf.urls.static import static
from django.contrib.staticfiles import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name= 'index'),
    path('eventos/', eventos, name= 'eventos'),
    # path('eventos/<slug:categoria>/', eventos),
    path('getEventos', getEventos, name= 'getEventos'),
    path('crear-evento', crearEvento, name= 'crear-evento'),
    path('evento/<str:id>', evento_detail, name = 'evento'),
    path('about', about, name = 'about'),
    path('static', views.serve),
    # path(r'^evento/(?P<id>top|new)/$', evento_detail, name = 'evento'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
handler404 = 'aplicaciones.principal.views.handler404'
handler500 = 'aplicaciones.principal.views.handler500'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)