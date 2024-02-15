from django.shortcuts import render

def addUser(request):
     return  render(request,'addUser.html')

def allUser(request):
     return  render(request,'allUser.html')

