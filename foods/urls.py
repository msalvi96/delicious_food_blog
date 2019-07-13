from django.urls import path, include
from . import views

urlpatterns = [
    path('create', views.create, name='create'),
    path('<int:food_id>', views.detail, name='detail'),
    path('<int:food_id>/likes', views.likes, name='likes'),
]