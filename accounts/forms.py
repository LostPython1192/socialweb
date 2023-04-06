from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm, TextInput, EmailInput

class UserCreateForm(UserCreationForm):
    
    class Meta:
        fields = ('username','email','password1','password2')
        email = forms.CharField(required=True)
        
        
        
        model = get_user_model()
        
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Display Name'
        
        self.fields['email'].label = 'Email Address'