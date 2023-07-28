from django.urls import path
from .views import *

urlpatterns = [
    path('', developer_list, name='developer_list'),
    path('<int:id>', developer_detail, name='developer_detail'),
    path('create', developer_create, name='developer_create'),
    path('update/<int:id>', developer_update, name='developer_update'),
    path('delete/<int:id>', developer_delete, name='developer_delete')
]
