from myapp_admin.models import *
from django.forms import ModelForm

class RoomForm(ModelForm):
    class Meta:
        model = AddRoom
        fields = ['room_name', 'description','status']