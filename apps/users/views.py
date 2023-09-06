from django.shortcuts import render
from .forms import *
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy


class Login(LoginView):
    template_name = 'users/login.html'
    authentication_form = CustomAuthenticationForm
    
    def get_success_url(self):
        return reverse_lazy('videos')
    

class Registration(CreateView):
    template_name = 'users/registration.html'
    form_class = CustomUserCreationForm
    
    def get_success_url(self):
        return reverse_lazy('login')
    
    
class Logout(LogoutView):
    next_page = reverse_lazy('login')
