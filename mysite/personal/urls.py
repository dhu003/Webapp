from django.urls import path
from django.urls import include
from . import views




urlpatterns = [ 
    path(r'', views.index, name='index'),
    path(r'contact/', views.contact, name='contact')
]



