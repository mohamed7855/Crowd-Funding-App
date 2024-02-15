from django.shortcuts import render,reverse,HttpResponse,redirect
from fundProject.models import *
from django.http import HttpResponse, HttpResponseRedirect


def mainPage(request):
    return  render(request,'index.html')

def addCategory(request):
    if request.method == 'POST':
        category_name = request.POST.get('categoryName')
        Categories.objects.create(categoryName=category_name)
        return redirect('addCategory') 
    categories = Categories.objects.all()
    return render(request, 'addCategory.html', {'categories': categories})

def deleteCategory(request):
    if request.method == 'POST':
        category_id = request.POST.get('categoryToDelete')
        category = Categories.objects.get(pk=category_id)
        category.delete()
    return redirect('addCategory')

def addProject(request):
     return  render(request,'fundProject/addProject.html')


def detailProject(request):
     return  render(request,'fundProject/detailProject.html')



