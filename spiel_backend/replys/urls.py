from django.urls import path
from django.urls.resolvers import URLPattern
from replys import views


urlpatterns = [
    path('all/',views.get_all_replys),
    path('new/',views.add_replys),
    path('del/',views.delete_reply)
]