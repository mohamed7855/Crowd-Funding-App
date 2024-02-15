from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def updateUser(request):
    return render(request,'updateUser.html')

def insertuser(request):
    return render(request,'insertspecificUser.html')
