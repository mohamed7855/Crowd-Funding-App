from django.shortcuts import render
from django.http import HttpResponse

<<<<<<< HEAD
# Create your views here.
def updateUser(request):
    return render(request,'updateUser.html')

def insertuser(request):
    return render(request,'insertspecificUser.html')
=======
def addUser(request):
     return  render(request,'addUser.html')

def allUser(request):
     return  render(request,'allUser.html')

>>>>>>> d0f8258be0e0d0476c7af31a2496f189b1ca276f
