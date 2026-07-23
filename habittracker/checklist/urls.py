from django.urls import path
from . import views

urlpatterns = [
    path('', views.AddTasks, name='add_tasks'),
]