from django.urls import path
from .views import *

urlpatterns = [
    path('', game_list, name='game_list'),
    path('<int:id>', game_detail, name='game_detail'),
    path('create', game_create, name='game_create'),
    path('update/<int:id>', game_update, name='game_update'),
    path('delete/<int:id>', game_delete, name='game_delete')
]