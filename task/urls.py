from django.urls import path

from task.views import TaskAPIView

urlpatterns = [
    path("task/", TaskAPIView.as_view()),
    path("task/<int:pk>/", TaskAPIView.as_view())
]