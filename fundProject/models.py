from django.db import models


class Categories(models.Model):
    categoryName = models.CharField(max_length=20)

# Create your models here.



class Project(models.Model):
     # user
     title = models.CharField(max_length=285)
     details = models.TextField()
     category = models.CharField()
     images = models.CharField()
     tags = models.TextField()
     totalTarget = models.DecimalField(max_digits=10, decimal_places=2)
     startTime = models.DateTimeField(auto_now=True)
     endTime = models.DateTimeField(auto_now=True)
     
     def __str__(self):
        return f"{self.title},{self.category}"
   
     @classmethod
     def projectList(self):
        return self.objects.all()
    
     @classmethod
     def projectDetails(self,id):
        return self.objects.get(id=id)
     
     @classmethod
     def projectDelete(self,id):
        return self.objects.filter(id=id).delete()

