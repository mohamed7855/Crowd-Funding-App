from django.shortcuts import render,reverse,redirect, get_object_or_404
from fundProject.models import *
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from .models import Categories
from .models import Images
from .models import Rate
from django.contrib import messages
from django.http import Http404
def mainPage(request):
    return  render(request,'index.html')

def addProject(request):
    categories = Categories.objects.all()
    if request.method == 'POST':
        project=Project.projectAdd(request)
        print('Project added', project.id)
        images = request.FILES.getlist('projectimage[]')
        if images:
                for i in images:
                    image = Images(img=i, project_id=project)
                    image.save()
        return HttpResponseRedirect(reverse('project.all'))
    return render(request,'fundProject/addProject.html', {'categories': categories})
# def addProject(request):
#     categories = Categories.objects.all()
#     if request.method == 'POST':
#         category_id = request.POST.get('category', None)
#         category = Categories.objects.get(id=category_id) if category_id else None
        
#         project = Project.projectAdd(
#             title=request.POST['title'],
#             details=request.POST['projectDetail'],
#             totalTarget=request.POST['target'],
#             category_id=category 
#         )
        
#         images = request.FILES.getlist('projectimage[]')
#         if images:
#             for img in images:
#                 image = Images.objects.create(img=img, project_id=project)
#                 image.save()
#         return HttpResponseRedirect(reverse('project.all'))
#     return render(request, 'fundProject/addProject.html', {'categories': categories})

def projectList(request):
    projects = Project.objects.all()
    for project in projects:
        setattr(project, 'img', Images.objects.filter(project_id=project))

    context = {'projects': projects}
    context['imgs']=Images.imageList()
    return  render(request,'index.html',context)


def formatDate(input_date):
    formatted_date = input_date.strftime('%Y-%m-%d')
    return formatted_date

def projectUpdate(request, id):
    project = Project.projectDetails(id)
    project.startTime = formatDate(project.startTime)
    project.endTime = formatDate(project.endTime)
    categories = Categories.objects.all()
    context = {'project': project, 'categories': categories}
    if request.method == 'POST':
        if request.POST.get('title', '') != '':
            Project.projectUpdate(request, id)
            return HttpResponseRedirect(reverse('project.all'))
        else:
            context['msg'] = 'Kindly fill all fields'
    return render(request, 'fundProject/updateProject.html', context)


# def projectUpdate(request,id):
#     project=Project.projectDetails(id)
#     project.startTime = formatDate(project.startTime)
#     project.endTime = formatDate(project.endTime)
#     context={'project':project}
#     if request.method == 'POST':
#             if (request.POST['title'] != ''):
#                 Project.projectUpdate(request,id)
#                 return HttpResponseRedirect(reverse('project.all'))
#             else:
#                 context['msg']='Kindly fill all fields'
#     return render(request,'fundProject/updateProject.html',context)

def projectDelete(request,id):
    Project.projectDelete(id)
    return HttpResponseRedirect(reverse('project.all'))


# def projectDetails(request,projectid):
#     obj=Project.projectDetails(projectid)
#     setattr(obj, 'img', Images.objects.filter(project_id=obj))
#     context={'project':obj}
#     return  render(request,'fundProject/detailProject.html',context)

def projectDetails(request,projectid):
    obj=Project.projectDetails(projectid)
    setattr(obj, 'img', Images.objects.filter(project_id=obj))
    last_rate = Rate.objects.filter(project_id=obj).order_by('-id').first()
    context={'project':obj, 'last_rate': last_rate}
    return  render(request,'fundProject/detailProject.html',context)


def add_rate(request, project_id):
    if request.method == 'GET':
        rate = request.GET.get('rate')
        if rate is not None and rate.isdigit():
            rate = int(rate)
            project = get_object_or_404(Project, pk=project_id)
            Rate.objects.create(project_id=project, rate=rate)
            return redirect('projectDetails', projectid=project_id)
       
    return redirect('projectDetails', projectid=project_id)


def addCategory(request):
    if request.method == 'POST':
        category_name = request.POST.get('categoryName')
        Categories.objects.create(categoryName=category_name)
        return redirect('addCategory') 
    categories = Categories.objects.all()
    return render(request, 'category/addCategory.html', {'categories': categories})

def allCategory(request):
    categories = Categories.objects.all()
    return render(request, 'category/allCategory.html', {'categories': categories})

def deleteCategory(request):
    if request.method == 'POST':
        category_id = request.POST.get('categoryToDelete')
        category = Categories.objects.get(pk=category_id)
        category.delete()
    return redirect('allCategory')




# def addProject(request):
#      return  render(request,'fundProject/addProject.html')


# def detailProject(request):
#      return  render(request,'fundProject/detailProject.html')

 
# def projectList(request, id):
    
#     return HttpResponse(f'the Project ID: {id}')


# def projectDetails(request, id):
    
#     return HttpResponse(f'the Project Details ID: {id}')


# def addCommentOnProject(request, id):
    
#     return HttpResponse(f'Comment on Project {id}')


# def reportComment(request, id):
    
#     return HttpResponse(f'report Comment on Project {id}')

    
# def cancelProject(request, id):
    
#     return HttpResponse(f'cancel Project {id}')





