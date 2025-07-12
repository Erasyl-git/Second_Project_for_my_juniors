from django.db import models

from projects.models import Project

from django.core.validators import MinValueValidator, MaxValueValidator


class Task(models.Model):

    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)

    title = models.CharField(max_length=100)
    details = models.TextField(max_length=300)

    priority = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    status = models.CharField(max_length=100)