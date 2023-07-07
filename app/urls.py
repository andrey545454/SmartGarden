from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('/nature_home', views.nature_home, name='nature_home'),
    path('/nature_outside', views.nature_outside, name='nature_outside'),

    path('/add_nature', views.add_nature, name='add_nature'),

    path('/sensors', views.sensors, name='sensors')
]