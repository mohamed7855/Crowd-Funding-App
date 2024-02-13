from django.shortcuts import render,HttpResponse

# Create your views here.

def mainPage(request):
     return  render(request,'index.html')

def addProject(request):
     return  render(request,'fundProject/addProject.html')


def detailProject(request):
     return  render(request,'fundProject/detailProject.html')



