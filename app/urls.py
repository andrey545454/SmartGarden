from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('/nature_home', views.nature_home, name='nature_home'),
    path('/nature_outside', views.nature_outside, name='nature_outside'),
    path('/last_nature_home', views.last_nature_home, name='last_nature_home'),

    path('/add_nature', views.add_nature, name='add_nature'),
    path('/timetable', views.timetable, name='timetable'),

    path('/sensors', views.sensors, name='sensors')
]