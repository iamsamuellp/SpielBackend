from django.urls import path
from .import views

urlpatterns = [
  path('all/',views.get_all_stories),
  # path('story/',views.get_single_stories),
  path('pub/',views.get_published_list),
  path('unpub/',views.get_unpublished_list),
  path('new/',views.new_story),
  path('de//',views.remove_story),
  path('<int:pk>/',views.story_detail),
]