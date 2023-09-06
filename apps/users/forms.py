from typing import Any, Dict
from django import forms
from .models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, request, *args, **kwargs):
        super().__init__(request, *args, **kwargs)

        self.fields['username'].widget = forms.TextInput(attrs={'class': 'input', 'placeholder': 'логин'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'пароль'})
        
        
class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget = forms.TextInput(attrs={'class': 'input', 'placeholder': 'логин'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'пароль'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'повтор пароль'})
        
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username',)