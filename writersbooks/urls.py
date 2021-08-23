from django.urls import path
from . import views


urlpatterns = [
    path("", views.get_writer, name='writers_none'),
    path("<int:id>", views.get_writer, name='writers')
]
