import re
from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages




# Create your views here.

def updateUser(request):
    return render(request,'updateUser.html')

def insertuser(request):
    return render(request,'insertspecificUser.html')

def addUser(request):
     return  render(request,'addUser.html')

def allUser(request):
     return  render(request,'allUser.html')

