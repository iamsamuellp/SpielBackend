from django.urls import path
from django.urls.resolvers import URLPattern
from comments import views


urlpatterns = [
    path('', views.Commentslist.as_view())
]