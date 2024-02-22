from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render , reverse
from django.http import HttpResponseRedirect
from .models import Users
from django.contrib.auth.models import User
from fundProject.models import Project



# Create your views here.

def register(request):
    if request.method == 'POST':
        u_form = UserRegisterForm(request.POST)
        p_form = ProfileUpdateForm(request.POST)

        if u_form.is_valid():
            u_form.save()
            u_form.save()
            username = u_form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        u_form = UserRegisterForm()
        p_form = ProfileUpdateForm()
    return render(request, 'users/register.html', {'u_form': u_form,'p_form': p_form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'projects':Project.objects.filter(creator=request.user.id)
    }

    return render(request, 'users/profile.html', context)


def DeleteAccount(request, user_id):
    if request.method == 'POST':
        user = User.objects.get(id=user_id)
        user.delete()
        return redirect('login')  
    else:
        return redirect('profile')
#===========================================================================

def updateUser(request, id):
    if request.method == 'POST':
        Users.userUpdate(request, id)
        return HttpResponseRedirect(reverse('allUser'))
    user = Users.userDetails(id)
    context = {'user': user}
    return render(request, 'updateUser.html', context)


def userdetails(request,id):
    userdete={"userdete":Users.userDetails(id)}
    return render(request,'insertspecificUser.html',userdete)

def deleteUser(request,id):
    Users.userDelete(id)
    r=reverse('allUser')
    return HttpResponseRedirect(r)
    # return redirect(request,'allUser.html')

def addUser(request):
    if(request.method=='POST'):
        Users.userAdd(request)
        return HttpResponseRedirect(reverse('allUser'))
    return  render(request,'addUser.html')


def allUser(request):
    context={'users':User.objects.all()} 
    return  render(request,'allUser.html',context)

#===========================================================================

