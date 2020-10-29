from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('', views.signin, name='user_login'),
    path('logout/', views.signout, name='user_logout'),
]
