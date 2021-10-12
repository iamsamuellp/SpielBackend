from django.urls import path
from django.urls.resolvers import URLPattern
from replys import views


urlpatterns = [
    path('',views.ReplysList.as_view())
]