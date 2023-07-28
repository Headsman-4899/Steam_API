from django.urls import path
from .views import *

urlpatterns = [
    path('', publisher_list, name='publisher_list'),
    path('<int:id>', publisher_detail, name='publisher_detail'),
    path('create', publisher_create, name='publisher_create'),
    path('update/<int:id>', publisher_update, name='publisher_update'),
    path('delete/<int:id>', publisher_delete, name='publisher_delete')
]
