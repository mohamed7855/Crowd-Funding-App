from django.shortcuts import render, redirect , reverse,HttpResponse
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

def mainPage(request):
     return  render(request,'index.html')

def addProject(request):
     return  render(request,'fundProject/addProject.html')


def detailProject(request):
     return  render(request,'fundProject/detailProject.html')


from .forms import ProjectForm

def addProjectForm(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("detailProject"))
    else:
        form = ProjectForm()
    return render(request, 'fundProject/addProjectForm.html', {'form': form})

