from django.shortcuts import render,HttpResponse

# Create your views here.

def mainPage(request):
    return  render(request,'index.html')
    # return HttpResponse("Hello omara World")