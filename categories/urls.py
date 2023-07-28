from django.urls import path
from .views import *

urlpatterns = [
    path('', category_list, name='category_list'),
    path('<int:id>', category_detail, name='category_detail'),
    path('create', category_create, name='category_create'),
    path('update/<int:id>', category_update, name='category_update'),
    path('delete/<int:id>', category_delete, name='category_delete')
]
