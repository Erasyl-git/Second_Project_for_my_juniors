from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from projects.models import Project
from task.models import Task

from task.serializers import TaskSerializer
from rest_framework.exceptions import NotFound
   



class TaskAPIView(APIView):

    seralizers_class = TaskSerializer

    def get (self,requests):


         queryset = Task.objects.all()

       
         return Response(self.seralizers_class(queryset, many=True).data, status=status.HTTP_200_OK)
    

    def post(self, request):

        project = request.data.get("project")

        title = request.data.get("title")

        details = request.data.get("details")

        priority = request.data.get("priority")

        status = request.data.get("status")

        task = Task.objects.create(project=project, title=title, details=details, priority=priority, status=status)

        task.save()


        return Response({"massege": "success create"})




    
    def get_object(self, **kwargs):

        return get_object_or_404(Task, pk=kwargs["pk"])
    

    
    def patch(self, request, *args, **kwargs):


        queryset = self.get_object(pk=kwargs["pk"])

        task = self.seralizers_class(queryset, data=request.data, partial=True)

        if task.is_valid():

            task.save()

            return Response({"message": "task update"}, status=status.HTTP_200_OK)
        return Response(task.errors, status=status.HTTP_400_BAD_REQUEST)
    


    def put(self, request, *args, **kwargs):

        queryset = self.get_object(pk=kwargs["pk"])

        task = self.seralizers_class(queryset, data=request.data)

        if task.is_valid():

            task.save()

            return Response({"message": "task update put metod"}, status=status.HTTP_200_OK)
        return Response(task.errors, status=status.HTTP_400_BAD_REQUEST)
    


    def delete(self, request, *args, **kwargs):

        queryset = self.get_object(pk=kwargs["pk"])

        id = queryset.id 

        queryset.delete()

        queryset.save()

        return({"message": f"delete task{id}"})









   


    
    
       
    




         


         

    

