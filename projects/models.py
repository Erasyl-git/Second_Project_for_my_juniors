from django.db import models

class Project(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)

    is_active = models.BooleanField(True,False)



