from django.urls import path
from django.urls.resolvers import URLPattern
from replys import views


urlpatterns = [
    path('all/',views.get_all_replys),
    path('new/<int:pk>/',views.add_replys)
]