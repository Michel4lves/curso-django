from django.urls import path

from cursodjango.vpreview.views import video, indice

app_name = 'vpreview'
urlpatterns = [
    path('<slug:slug>', video, name='video'),
    path('', indice, name='indice'),
]
