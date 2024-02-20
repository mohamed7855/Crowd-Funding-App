from django.shortcuts import render , reverse
from django.http import HttpResponseRedirect
from .models import User

# Create your views here.
# def updateUser(request,id):
#     # userdete={'userdete':User.userUpdate(id)}
#     userdete={"userdete":User.userDetails(id)}
#     if(request.method=='POST'):
#         User.userUpdate(request,id)
#         return HttpResponseRedirect(reverse('allUser'))
#     return render(request,'updateUser.html',userdete)

def updateUser(request, id):
    user = User.userDetails(id)
    context = {'user': user}
    if request.method == 'POST':
        User.userUpdate(request, id)
        return HttpResponseRedirect(reverse('allUser'))
    return render(request, 'updateUser.html', context)


def userdetails(request,id):
    userdete={"userdete":User.userDetails(id)}
    return render(request,'insertspecificUser.html',userdete)

def deleteUser(request,id):
    User.userDelete(id)
    r=reverse('allUser')
    return HttpResponseRedirect(r)
    # return redirect(request,'allUser.html')

def addUser(request):
    if(request.method=='POST'):

        User.userAdd(request)
        return HttpResponseRedirect(reverse('allUser'))
    return  render(request,'addUser.html')


def allUser(request):
    context={'users':User.userList()} 
    return  render(request,'allUser.html',context)

