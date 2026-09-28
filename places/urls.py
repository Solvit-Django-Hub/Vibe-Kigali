from django.urls import path
from . import views

urlpatterns = [
    path('', views.PlaceListCreateView.as_view(), name='place-list'),
    path('<int:pk>/', views.PlaceDetailView.as_view(), name='place-detail'),
]
