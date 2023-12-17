from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import CustomUser  # Import your custom user model

def register(request):
    # Registration logic here

def activate(request, uidb64, token):
    # Email confirmation logic here

