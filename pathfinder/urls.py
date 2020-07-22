from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('creategrid',views.creategrid,name='creategrid'),
    path('searchpath',views.searchpath,name='searchpath')
]