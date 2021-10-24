from django.urls import path
from django.urls.resolvers import URLPattern
from comments import views


urlpatterns = [
    path('all/', views.get_all_comments),
    path('new/', views.new_comment),
    path('del/', views.edit_comment)
]