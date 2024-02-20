from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')


def updateUser(request):
    return render(request,'updateUser.html')

def insertuser(request):
    return render(request,'insertspecificUser.html')

def addUser(request):
     return  render(request,'addUser.html')

def allUser(request):
     return  render(request,'allUser.html')

