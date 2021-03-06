"""
Como agregar un URL

Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')

Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
"""

from django.conf.urls import url, include
from django.contrib import admin
from gestion import views

app_name = "gestion"

urlpatterns = [
    url(r'^$', views.Dashboard.as_view(), name='dashboard'),
    url(r'^profesores$', views.ListarProfesores.as_view(), name='listar'),
    url(r'^profesores/agregar/$', views.AgregarProfesor.as_view(), name='agregar'),
    url(r'^profesores/editar/(?P<pk>[-\w]+)/$', views.EditarProfesor.as_view() , name='editar'),
    url(r'^profesores/eliminar/(?P<pk>[-\w]+)/$', views.EliminarProfesor.as_view() , name='eliminar'),
    url(r'^profesores/(?P<pk>[-\w]+)/$', views.VerProfesor.as_view(), name='ver'),
]
