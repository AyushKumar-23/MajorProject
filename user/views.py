from django.shortcuts import render
from django.urls import reverse_lazy
from . import forms
from django.views.generic import CreateView

# Create your views here.
class UserRegisterView(CreateView):
    form_class = forms.SingUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')