from django.urls import path
from .views import *

urlpatterns = [
    path('', review_list, name='review_list'),
    path('<int:id>', review_detail, name='review_detail'),
    path('create', review_create, name='review_create'),
    path('update/<int:id>', review_update, name='review_update'),
    path('delete/<int:id>', review_delete, name='review_delete')
]
