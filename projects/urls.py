from django.urls import path

from projects.views import ProjectAPIView

urlpatterns = [
    path("project/", ProjectAPIView.as_view()),
    path("project/<int:pk>/", ProjectAPIView.as_view()),
]