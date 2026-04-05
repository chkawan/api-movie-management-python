from django.urls import path
from . import views



urlpatterns = [
    #GENRES
    path('genres/', views.GenreCreateListView.as_view(), name='genre-list'),
    path('genres/<int:pk>/', views.GenreRetrieveUpdateDestroyView.as_view(), name='genre-detail-view'),
]