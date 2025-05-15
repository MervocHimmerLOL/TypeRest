from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.models import User
from django.contrib import messages

from user.form import RegisterForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account {username} created')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'user/register.html', {'form': form})

def profile(request):
    return render(request, 'user/profile.html')
