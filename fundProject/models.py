from django.db import models

from user.models import User

class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    categoryName = models.CharField(max_length=20, unique=True )
    def __str__(self):
        return self.categoryName
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['categoryName'], name='unique_category_name')
        ]
class Project(models.Model):
    title = models.CharField(max_length=285)
    details = models.TextField()
    totalTarget = models.DecimalField(max_digits=10, decimal_places=2)
    startTime = models.DateTimeField(auto_now=True)
    endTime = models.DateTimeField(auto_now=True)
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE,null=True)
     
     
    def _str_(self):
        return f"{self.title}"
   
    @classmethod
    def projectList(self):
        return self.objects.all()
    
    @classmethod
    def projectDetails(self,id):
        return self.objects.get(id=id)
     
    @classmethod
    def projectDelete(self,id):
        return self.objects.filter(id=id).delete()

    #  @classmethod
    #  def projectAdd(self,request):
    #     category_id = request.POST.get('category', None)
    #     category = Categories.objects.get(id=category_id) if category_id else None
    #     return self.objects.create(title=request.POST['title'],
    #                                details=request.POST['projectDetail'],
    #                                totalTarget=request.POST['target'],
    #                                category_id=category,
    #                             #    image=request.FILES['pImage'],
    #                             #    count=request.POST['pCount'],
    #                             #    category=Category.objects.get(id=request.POST['pCategory'])
    #                             )
    @classmethod
    def projectAdd(cls, request):
        category_id = request.POST.get('category', None)
        category = Categories.objects.get(id=category_id) if category_id else None
        
        project = cls.objects.create(
            title=request.POST['title'],
            details=request.POST['projectDetail'],
            totalTarget=request.POST['target'],
            category_id=category
        )

        tags = request.POST.get('tags', '').split(',')
        for tag_name in tags:
            tag = Tags.objects.create(project_id=project, tag_name=tag_name.strip())
        
        return project

     
    #  @classmethod
    #  def projectUpdate(self,request,id):
    #     category_id = request.POST.get('category', None)
    #     category = Categories.objects.get(id=category_id) if category_id else None
    #     return self.objects.filter(id=id).update(
    #                             title=request.POST['title'],
    #                             details=request.POST['projectDetail'],
    #                             totalTarget=request.POST['target'],
    #                             category_id=category 
    #                             # image=request.POST['pImage'],
    #                             # count=request.POST['pCount'],
    #                             # category=Category.objects.get(id=request.POST['pCategory'])
    #                             )
    @classmethod
    def projectUpdate(cls, request, id):
            category_id = request.POST.get('category', None)
            category = Categories.objects.get(id=category_id) if category_id else None
            
            cls.objects.filter(id=id).update(
                title=request.POST['title'],
                details=request.POST['projectDetail'],
                totalTarget=request.POST['target'],
                category_id=category
            )

            project = cls.objects.get(id=id)
            Tags.delete_tags_for_project(project)
            tags = request.POST.get('tags', '').split(',')
            for tag_name in tags:
                tag = Tags.objects.create(project_id=project, tag_name=tag_name.strip())


class Tags(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    tag_name = models.CharField(max_length=40)

    @classmethod
    def delete_tags_for_project(cls, project):
        cls.objects.filter(project_id=project).delete()
        
    
class Images (models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    img = models.ImageField(blank=False, null=False, upload_to='fundProject/images')
    
    # Instance methods
    def getImgURL(self): 
        return f"/media/{self.img}"
    
    @classmethod
    def imageList(self):
        return self.objects.all()
    
    def _str_(self):
        return f"{self.img}"
    
    
# class Tags (models.Model):
#     project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
#     tag_name = models.CharField(max_length=40)


    
class Donation(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    donation_value = models.IntegerField()


class Rate(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    rate = models.IntegerField()


class Comment(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    comment = models.TextField(default='')
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class CommentReports(models.Model):
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)



class ProjectReports(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    message = models.CharField(max_length=100)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)



