from django.db import models

from projects.models import Project










class Task(models.Model):

    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)

    title = models.CharField(max_length=100)
    details = models.TextField(max_length=300)

    prority = models.IntegerField(max_length=5)
    status = models.CharField(max_length=100)