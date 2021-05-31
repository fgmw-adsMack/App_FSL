from django.urls import path
from django.conf.urls import url
from . import views
from .views import ItemDetailView

urlpatterns = [
    path('register_movie/', views.register_movie, name='register_movie'),
    path('register_book/', views.register_book, name='register_book'),
    path('register_series/', views.register_series, name='register_series'),
    path('<int:item_id>', views.detail, name='item_detail'),
    path('<int:item_id>/evaluation', views.evaluation, name='evaluation'),
    url('^like/$', views.like, name='like'),
]
