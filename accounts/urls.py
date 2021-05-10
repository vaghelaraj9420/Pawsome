from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path("signup", views.signup, name="signup"),
    path("csignup", views.csignup, name="csignup"),
    path("login",views.login, name="login"),
    path("logout",views.logout,name="logout"),


]
