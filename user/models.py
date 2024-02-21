from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import uuid
from django.utils import timezone

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    image = models.ImageField(default='default.jpg', upload_to='user/images', null=True)

    def __str__(self):
        return f'{self.user.username} Profile'
    
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.image.path)

    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)

class AdditionalInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=None)
    birthdate = models.DateField()
    country = models.CharField(max_length=20)
    facebook = models.URLField(max_length=200)


class ProfileActivation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
class Activation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now)

    def is_expired(self):
        return (timezone.now() - self.created_at).days >= 1

# class User(models.Model):    
#     firstName=models.TextField()
#     lastName=models.TextField()
#     email=models.EmailField()
#     password=models.TextField()
#     confirmPass=models.TextField()
#     mobilPhone=models.TextField()
#     photo=models.TextField()
#     is_active = models.BooleanField(default=False)

#     @classmethod
#     def userList(self):
#         return self.objects.all()
    
#     @classmethod
#     def userDetails(self,id):
#         return self.objects.get(id=id)
    

#     @classmethod
#     def userDelete(self,id):
#         return self.objects.filter(id=id).delete()
    
#     @classmethod
#     def userAdd(self,request):
#         return self.objects.create(firstName=request.POST['uFirstName'],
#                                    lastName=request.POST['uLastName'],
#                                    email=request.POST['uEmail'],
#                                    password=request.POST['uPassword'],
#                                    confirmPass=request.POST['uConfirmPass'],
#                                    mobilPhone=request.POST['uMobilPhone'],
#                                    photo=request.FILES['uImage'],
#                                    )
#     @classmethod
#     def userUpdate(self,request,id):
#         return self.objects.filter(id=id).update(
#                                 firstName=request.POST['uFirstName'],
#                                 lastName=request.POST['uLastName'],
#                                 email=request.POST['uEmail'],
#                                 password=request.POST['uPassword'],
#                                 confirmPass=request.POST['uConfirmPass'],
#                                 mobilPhone=request.POST['uMobilPhone'],
#                                 photo=request.POST['uImage'],
#                                 )


