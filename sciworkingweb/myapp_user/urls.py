from django.urls import path, re_path
from .views import *
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    #path('', views.home, name='home'),
    path('', CalendarView.as_view(), name='calendar'),
    path('event', views.event, name='event_new'),
    path('user_mybooking', views.user_mybooking, name='user_mybooking'),
    path('user_profile', views.user_profile, name='user_profile'),
    path('alerts', views.alerts, name='alerts'),
    
]
