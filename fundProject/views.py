from django.shortcuts import render,reverse,redirect
from fundProject.models import *
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from .models import Images

def mainPage(request):
    return  render(request,'index.html')

def addProject(request):
    if request.method == 'POST':
        print('aaaaaaaaaaaaaaaaaaaaaaaaaaa')
        project=Project.projectAdd(request)
        print('aaaaaaaaaaaaaaaaaaaaaaaaaaa2222')

        print('Project added', project.id)
        images = request.FILES.getlist('projectimage[]')
        if images:
                for i in images:
                    image = Images(img=i, project_id=project)
                    image.save()
        return HttpResponseRedirect(reverse('project.all'))
    return render(request,'fundProject/addProject.html')

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

def projectUpdate(request,id):
    project=Project.projectDetails(id)
    project.startTime = formatDate(project.startTime)
    project.endTime = formatDate(project.endTime)
    context={'project':project}
    if request.method == 'POST':
            if (request.POST['title'] != ''):
                Project.projectUpdate(request,id)
                return HttpResponseRedirect(reverse('project.all'))
            else:
                context['msg']='Kindly fill all fields'
    return render(request,'fundProject/updateProject.html',context)

def projectDelete(request,id):
    Project.projectDelete(id)
    return HttpResponseRedirect(reverse('project.all'))


def projectDetails(request,projectid):
    obj=Project.projectDetails(projectid)
    setattr(obj, 'img', Images.objects.filter(project_id=obj))

    context={'project':obj}
    return  render(request,'fundProject/detailProject.html',context)





# def addCategory(request):
#     if request.method == 'POST':
#         category_name = request.POST.get('categoryName')
#         Categories.objects.create(categoryName=category_name)
#         return redirect('addCategory') 
#     categories = Categories.objects.all()
#     return render(request, 'addCategory.html', {'categories': categories})


# def deleteCategory(request):
#     if request.method == 'POST':
#         category_id = request.POST.get('categoryToDelete')
#         category = Categories.objects.get(pk=category_id)
#         category.delete()
#     return redirect('addCategory')


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





