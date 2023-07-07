from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/nature', views.nature, name='nature'),
    path('/add_nature', views.add_nature, name='add_nature'),
]