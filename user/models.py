from django.db import models

# Create your models here.

class User(models.Model):    
    firstName=models.TextField()
    lastName=models.TextField()
    email=models.EmailField()
    password=models.TextField()
    confirmPass=models.TextField()
    mobilPhone=models.TextField()
    photo=models.TextField()


    @classmethod
    def userList(self):
        return self.objects.all()
    
    @classmethod
    def userDetails(self,id):
        return self.objects.get(id=id)
    

    @classmethod
    def userDelete(self,id):
        return self.objects.filter(id=id).delete()
    
    @classmethod
    def userAdd(self,request):
        return self.objects.create(firstName=request.POST['uFirstName'],
                                   lastName=request.POST['uLastName'],
                                   email=request.POST['uEmail'],
                                   password=request.POST['uPassword'],
                                   confirmPass=request.POST['uConfirmPass'],
                                   mobilPhone=request.POST['uMobilPhone'],
                                   photo=request.FILES['uImage'],
                                   )
    @classmethod
    def userUpdate(self,request,id):
        return self.objects.filter(id=id).update(
                                firstName=request.POST['uFirstName'],
                                lastName=request.POST['uLastName'],
                                email=request.POST['uEmail'],
                                password=request.POST['uPassword'],
                                confirmPass=request.POST['uConfirmPass'],
                                mobilPhone=request.POST['uMobilPhone'],
                                photo=request.POST['uImage'],
                                )


