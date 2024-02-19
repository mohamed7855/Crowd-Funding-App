from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def updateUser(request):
    return render(request,'updateUser.html')

def insertuser(request):
    return render(request,'insertspecificUser.html')

def addUser(request):
     return  render(request,'addUser.html')

def allUser(request):
     return  render(request,'allUser.html')

