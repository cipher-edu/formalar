from django import forms
from .models import *

class RegisterForm(forms.ModelForm):
    class Meta:

        model = Register
        fields = '__all__'
        widgets = {
            'user_name': forms.TextInput(attrs={'class':'form-control'})
        }