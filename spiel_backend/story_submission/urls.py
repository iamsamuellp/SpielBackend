from django.urls import path
from .import views

urlpatterns = [
  path('', views.StoryList.as_view())
]