

from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'), # url открытия кулинарных книг
    path('open/<int:pk>/', views.open, name='open'),# url открытия описание рецептов
    path('auth/', views.auth, name='auth'),# url открытия инф об авторах
]
