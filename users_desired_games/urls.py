from django.urls import path
from .views import *

urlpatterns = [
    path('', user_desired_games_list, name='user_desired_games_list'),
    path('<int:id>', user_desired_games_detail, name='user_desired_games_detail'),
    path('create', user_desired_games_create, name='user_desired_games_create'),
    path('update/<int:id>', user_desired_games_update, name='user_desired_games_update'),
    path('delete/<int:id>', user_desired_games_delete, name='user_desired_games_delete')
]