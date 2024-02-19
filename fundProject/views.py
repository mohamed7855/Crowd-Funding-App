from django.shortcuts import render,reverse,redirect, get_object_or_404
from fundProject.models import *
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from .models import Categories
from .models import Images
from .models import Rate
from django.contrib import messages
from django.http import Http404
from django.db.models import Sum

from django.contrib.auth.decorators import login_required


def mainPage(request):
    return  render(request,'fundProject/home.html')

@login_required()
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

def projectList(request):
    projects = Project.objects.all()
    for project in projects:
        setattr(project, 'img', Images.objects.filter(project_id=project))

    context = {'projects': projects}
    context['imgs']=Images.imageList()
    return  render(request,'fundProject/home.html',context)


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



def projectDelete(request, id):
    project = Project.objects.get(id=id)
    total_donations = Donation.objects.filter(project_id=project).aggregate(total_donations=Sum('donation_value'))['total_donations']
    total_target_float = float(project.totalTarget)
    if total_donations is not None and total_donations > total_target_float * 0.25:
        messages.error(request, 'Cannot delete project: total donations exceed 25% of the total target.')
    else:
        Project.projectDelete(id)
        messages.error(request, 'Succuess Delete Project')
    return HttpResponseRedirect(reverse('project.all'))


def projectDetails(request, projectid):
    obj = Project.projectDetails(projectid)
    setattr(obj, 'img', Images.objects.filter(project_id=obj))
    last_rate = Rate.objects.filter(project_id=obj).order_by('-id').first()
    sum_donate = Donation.objects.filter(project_id=obj).aggregate(Sum('donation_value'))['donation_value__sum']
    comments = Comment.objects.filter(project_id=obj)  
    context = {'project': obj, 'last_rate': last_rate, 'sum_donate': sum_donate, 'comments': comments}
    return render(request, 'fundProject/detailProject.html', context)

def comment(request, id):
    obj = Project.projectDetails(id)
    if request.method == 'POST':
        comment_text = request.POST.get('comment_text')
        if comment_text:
            Comment.objects.create(project_id=obj, comment=comment_text)
    comments = Comment.objects.filter(project_id=obj)
    context = {'project': obj, 'comments': comments}
    return render(request, 'fundProject/comment.html', context)

def CommentDelete(request, id, comment_id):
    obj = Project.projectDetails(id)
    comments = Comment.objects.filter(project_id=obj)
    comment = get_object_or_404(comments, pk=comment_id)
    if request.method == 'POST':
        comment.delete()
        return redirect('comment', id=id)  
    return redirect('comment', id=id)  


def add_rate(request, project_id):
    if request.method == 'GET':
        rate = request.GET.get('rate')
        if rate is not None and rate.isdigit():
            rate = int(rate)
            if 0 <= rate <= 10:  
                project = get_object_or_404(Project, pk=project_id)
                Rate.objects.create(project_id=project, rate=rate)
                return redirect('projectDetails', projectid=project_id)
            else:
                messages.error(request, 'Rate must be between 0 and 10.')
        else:
            messages.error(request, 'Rate must be Postive Number')
    return redirect('projectDetails', projectid=project_id)

def add_donate(request, project_id):
    if request.method == 'GET':
        donation_value = request.GET.get('donation_value')
        if donation_value is not None and donation_value.isdigit():
            donation_value = int(donation_value)
            if donation_value > 0: 
                project = get_object_or_404(Project, pk=project_id)
                Donation.objects.create(project_id=project, donation_value=donation_value)
                return redirect('projectDetails', projectid=project_id)
            else:
                messages.error(request, 'Donation value must be a positive number.')
        else:
            messages.error(request, 'Invalid donation value.')
    return redirect('projectDetails', projectid=project_id)

def addCategory(request):
    if request.method == 'POST':
        category_name = request.POST.get('categoryName')
        if Categories.objects.filter(categoryName=category_name).exists():
            messages.error(request, 'Category with this name already exists.')
            return redirect('addCategory')
        else:
            Categories.objects.create(categoryName=category_name)
            return redirect('allCategory') 
        Categories.objects.create(categoryName=category_name)
        return HttpResponseRedirect(reverse('allCategory'))
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




# def add_all_Comment(request, id):
#     if request.method == 'POST':
#         comment_text = request.POST.get('comment_text')
#         if comment_text:
#             project = Project.objects.get(pk=id)
#             Comment.objects.create(project_id=project, comment=comment_text)
#     # Redirect back to the project detail page
#     return redirect('projectDetails', projectid=id)

# def add_all_Comment(request, id):
#     if request.method == 'POST':
#         comment = request.POST.get('comment')
#         if comment:
#             project = Project.objects.get(pk=id)
#             Comment.objects.create(project_id=project, comment=comment)
#             return redirect('add_all_Comment') 
#     comments = Comment.objects.all()
#     return render(request, 'fundProject/comment.html', {'comments': comments})

# def projectDetails(request,projectid):
#     obj=Project.projectDetails(projectid)
#     setattr(obj, 'img', Images.objects.filter(project_id=obj))
#     context={'project':obj}
#     return  render(request,'fundProject/detailProject.html',context)


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

