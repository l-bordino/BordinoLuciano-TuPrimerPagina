from django.urls import path
from django.urls import include
from inicio import templates, views
from inicio.views import inicio 

urlpatterns = [
    path('', inicio, name='inicio'),
]
