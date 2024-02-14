from django.db import models

class Categories(models.Model):
    categoryName = models.CharField(max_length=20)

class Project(models.Model):
     title = models.CharField(max_length=285)
     details = models.TextField()
     tags = models.TextField()
     totalTarget = models.DecimalField(max_digits=10, decimal_places=2)
     startTime = models.DateTimeField(auto_now=True)
     endTime = models.DateTimeField(auto_now=True)
     category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
     
     
     
     
     
     
     
     
     def _str_(self):
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

class Images (models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    img = models.ImageField(blank=False, null=False, upload_to='fundProject/images')