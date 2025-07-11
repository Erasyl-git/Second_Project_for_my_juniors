
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Project
from .models import Task


from serializers import ProjctSerializer
from serializers import TaskSerializer
   



class TaskAPIView(APIView):

    seralizers_class = TaskSerializer

    def get (self,requests):


         queryset = Task.objects.all()

       
         return Response(self.seralizers_class(queryset, many=True).data, status=status.HTTP_200_OK)
    




    def get (self,request):
         
        
        title = request.data.get("title")

        details = request.data.get("details")

        priority = request.data.get("priority")
        status = request.data.get("status")





    def post(self,request):

        project = Project.objects.crate(title=title,   description=description, is_active=is_active)

        title = request.data.get("title")

        details = request.data.get("details")

        priority = request.data.get("priority")
        status = request.data.get("status")

    




         


         

    

