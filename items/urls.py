from django.urls import path
from . import views
from .views import ItemDetailView

urlpatterns = [
    path('register_movie/', views.register_movie, name='register_movie'),
    path('register_book/', views.register_book, name='register_book'),
    path('register_series/', views.register_series, name='register_series'),
    path('<int:pk>', ItemDetailView.as_view(), name='item_detail'),
]
