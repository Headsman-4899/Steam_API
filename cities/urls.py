from django.urls import path
from .views import *

urlpatterns = [
    path('', city_list, name='city_list'),
    path('<int:id>/', city_detail, name='city_detail'),
    path('create', city_create, name='city_create'),
    path('update/<int:id>', city_update, name='city_update'),
    path('delete/<int:id>', city_delete, name='city_delete'),
]
