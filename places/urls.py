from django.urls import path
from . import views

urlpatterns = [
    path('', views.place_list, name='place-list'),
    path('<int:pk>/', views.place_detail, name='place-detail'),
]