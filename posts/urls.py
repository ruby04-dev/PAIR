# posts/urls.py
from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('<int:post_pk>/edit/', views.edit, name='edit'),
    path('<int:post_pk>/delete/', views.delete, name='delete'), 
    path('<int:post_pk>/update/', views.update, name='update'), 
]