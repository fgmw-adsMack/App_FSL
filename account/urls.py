from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls import url

urlpatterns = [
    path(
        'login/',
        auth_views.LoginView.as_view(redirect_authenticated_user=True),
        name='login',
    ),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.index, name='index'),
    path('signup/', views.creation_user_profile, name='signup'),
    path('edit/', views.update_profile, name='edit'),
    url(r'^password/$', views.change_password, name='change_password'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('<slug:slug>', views.profile_detail, name='profile_detail'),
    path('search/', views.members_itens_search, name='search'),
]
