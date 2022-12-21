from django.urls import path
from myapp_admin.views import *
from . import views

urlpatterns = [  
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    
    path('admin_room/', views.admin_room, name='admin_room'), 
    path('delete_room/<int:id>',views.delete_room, name="delete_room"),
    path('edit_room/<int:id>',views.edit_room, name="edit_room"),
    
    path('admin_user/', views.admin_user, name='admin_user'),
    path('admin_profile/', views.admin_profile, name='admin_profile'),
    path('admin_alerts/', views.admin_alerts, name='admin_alerts'),
]
