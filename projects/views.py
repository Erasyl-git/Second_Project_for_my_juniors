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

        

