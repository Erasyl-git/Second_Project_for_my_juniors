
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Project
from .models import Task


from serializers import ProjctSerializer
from serializers import TaskSerializer
