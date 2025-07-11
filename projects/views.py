from rest_framework.views import APIView

from rest_framework import status

from rest_framework.response import Response

from rest_framework.exceptions import NotFound

from django.shortcuts import get_object_or_404

from projects.models import Project

from projects.serializers import ProjectSerializer

class ProjectAPIView(APIView):

    serializer_class = ProjectSerializer

    def get(self, request):

        queryset = Project.objects.all()

        return Response(self.serializer_class(queryset, many=True).data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):

        title = request.data.get("title")

        description = request.data.get("description")

        is_active = request.data.get("is_active")

        project = Project.objects.create(title=title, description=description, is_active=is_active)

        project.save()

        return Response({"massege": "success create"})
    
    def get_object(self, **kwargs):

        return get_object_or_404(Project, pk=kwargs["pk"])
    
    def patch(self, request, *args, **kwargs):

        queryset = self.get_object(pk=kwargs["pk"])

        project = self.serializer_class(queryset, data=request.data, partial=True)

        if project.is_valid():

            project.save()

            return Response({"message": "project update"}, status=status.HTTP_200_OK)
        return Response(project.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, *args, **kwargs):

        queryset = self.get_object(pk=kwargs["pk"])

        project = self.serializer_class(queryset, data=request.data)

        if project.is_valid():

            project.save()

            return Response({"message": "project update put metod"}, status=status.HTTP_200_OK)
        return Response(project.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, *args, **kwargs):

        queryset = self.get_object(pk=kwargs["pk"])

        id = queryset.id 

        queryset.delete()

        queryset.save()

        return({"message": f"delete project{id}"})

        







