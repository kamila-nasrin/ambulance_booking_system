from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django import forms
# from django.forms.models import ModelForm
from django.forms.widgets import FileInput

class CreateUserForm(UserCreationForm):
    class meta:
        model=User
        fields=['username','password1','password2']
        
class Driv_profForm(forms.ModelForm):
    class Meta:
        model = Driv_prof
        fields = '__all__'
        exclude=['user']
        widgets={
            'ambulance_image':FileInput(),
        }
        labels={
            'phone_num':"Phone number",
            'vehicle_num':"Vehicle number",
            'amb_type':"Ambulance type",
            'amb_status':"Ambulance status",
        }

class BookingsForm(forms.ModelForm):
    class Meta:
        model=Bookings
        fields=['Name','Place','email','Phone_number']
        
        

        

