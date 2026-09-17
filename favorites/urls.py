from django.urls import path
from . import views

urlpatterns = [
    path('', views.favorite_list, name='favorite-list'),
]