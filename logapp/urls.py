from django.urls import path

from . import views

urlpatterns = [
    path('welcome', views.welcome, name="welcome"),
    path('register', views.register, name="register"),
    path('logout', views.logout, name="logout"),
    path('', views.home, name="home"),
]