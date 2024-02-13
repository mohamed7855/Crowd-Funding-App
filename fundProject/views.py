from django.shortcuts import render,HttpResponse,redirect
from fundProject.models import Categories

# Create your views here.

def mainPage(request):
<<<<<<< HEAD
    return  render(request,'index.html')
    # return HttpResponse("Hello omara World")
    
    


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
=======
     return  render(request,'index.html')

def addProject(request):
     return  render(request,'fundProject/addProject.html')


def detailProject(request):
     return  render(request,'fundProject/detailProject.html')



>>>>>>> 8aefb0271c49108c9d7d29ee238499395d4cbd7d
