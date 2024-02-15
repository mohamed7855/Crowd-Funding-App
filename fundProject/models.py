from django.db import models



from user.models import User
class Categories(models.Model):
    categoryName = models.CharField(max_length=20)

class Project(models.Model):
     title = models.CharField(max_length=285)
     details = models.TextField()
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
    
    
class Tags (models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    tag_name = models.CharField(max_length=40)


class Donation(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    donation_value = models.IntegerField()


class Rate(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    rate = models.IntegerField()


class Comment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    comment = models.TextField(default='')


class CommentReports(models.Model):
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)



class ProjectReports(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    message = models.CharField(max_length=100)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)



