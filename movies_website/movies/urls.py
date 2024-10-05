from django.urls import path
from . import views

app_name = 'movie'

urlpatterns = [
    path('', views.movie_list, name='list'), 
    path('add/', views.movie_add, name='add'), 
    path('<slug:slug>/', views.movie_detail, name='detail'), 
]
