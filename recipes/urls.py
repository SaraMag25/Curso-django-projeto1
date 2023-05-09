from .  import views
from django.urls import path

urlpatterns = [
    path('',views.home),
    path('contato/',views.contato),
    path('sobre',views.Sobre),
]