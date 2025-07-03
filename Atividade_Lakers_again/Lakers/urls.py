from django.urls import path
from . import views

urlpatterns = [
path("", views.index, name="index"),
path("", views.elenco, name="elenco"),
path("", views.sobre, name="sobre"),
path("", views.contato, name="contato"),
]