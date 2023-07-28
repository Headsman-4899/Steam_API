from django.urls import path
from .views import *

urlpatterns = [
    path('', user_list, name='user_list'),
    path('<int:id>', user_detail, name='user_detail'),
    path('create', user_create, name='user_create'),
    path('update/<int:id>', user_update, name='user_update'),
    path('delete/<int:id>', user_delete, name='user_delete')
]