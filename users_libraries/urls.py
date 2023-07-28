from django.urls import path
from .views import *

urlpatterns = [
    path('', user_library_list, name='user_library_list'),
    path('<int:id>', user_library_detail, name='user_library_detail'),
    path('create', user_library_create, name='user_library_create'),
    path('update/<int:id>', user_library_update, name='user_library_update'),
    path('delete/<int:id>', user_library_delete, name='user_library_delete')
]
