from django.urls import path
from .views import *

urlpatterns = [
    path('', system_requirements_list, name='system_requirements_list'),
    path('<int:id>', system_requirements_detail, name='system_requirements_detail'),
    path('create', system_requirements_create, name='system_requirements_create'),
    path('update/<int:id>', system_requirements_update, name='system_requirements_update'),
    path('delete/<int:id>', system_requirements_delete, name='system_requirements_delete')
]