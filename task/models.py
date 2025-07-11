from django.db import models



class Project(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)

    is_active = models.BooleanField(True,False)







class Task(models.Model):

    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)

    title = models.CharField(max_length=100)
    details = models.TextField(max_length=300)

    priority = models.IntegerField(max_length=5)
    status = models.CharField(max_length=100)