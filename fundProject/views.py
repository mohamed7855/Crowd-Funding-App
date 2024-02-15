from django.shortcuts import render, redirect , reverse,HttpResponse
from django.shortcuts import render,HttpResponse,redirect
from fundProject.models import *
from django.http import HttpResponse, HttpResponseRedirect

from .forms import ProjectForm
def mainPage(request):
    return  render(request,'index.html')
<<<<<<< HEAD
    
    

=======
>>>>>>> 690dbab8e08370902ded6d43d1ad9dd7e3723a4e

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

 
def projectList(request, id):
    
    return HttpResponse(f'the Project ID: {id}')


def projectDetails(request, id):
    
    return HttpResponse(f'the Project Details ID: {id}')


def addCommentOnProject(request, id):
    
    return HttpResponse(f'Comment on Project {id}')


def reportComment(request, id):
    
    return HttpResponse(f'report Comment on Project {id}')

    
def cancelProject(request, id):
    
    return HttpResponse(f'cancel Project {id}')





def addProjectForm(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("detailProject"))
    else:
        form = ProjectForm()
    return render(request, 'fundProject/addProjectForm.html', {'form': form})
