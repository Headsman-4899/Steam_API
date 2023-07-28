from django.urls import path
from .views import *

urlpatterns = [
    path('', country_list, name='country_list'),
    path('<int:id>/', country_detail, name='country_detail'),
    path('create', country_create, name='country_create'),
    path('update/<int:id>', country_update, name='country_update'),
    path('delete/<int:id>', country_delete, name='country_delete')
]
