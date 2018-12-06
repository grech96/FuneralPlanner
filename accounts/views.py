from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy

# Create your views here.

class SignUp (generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('/')
    template_name = 'signup.html'