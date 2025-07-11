from rest_framework import serializers


from .models import Project



from .models import Task


class ProjctSerializer(serializers.ModelSerializer):

    class Meta:

        model = Project
        fields = ["title", "description", "is_active"]





class TaskSerializer(serializers.ModelSerializer):

    class Meta:

        model = Task
        fields = ["title", "details", "prority", "status"]
