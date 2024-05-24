

from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('open/<int:pk>/', views.open, name='open'),
    #path('tasks/delete/<int:pk>/', views.remove_task, name='remove_task'),
]
