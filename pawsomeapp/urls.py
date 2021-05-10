"""pawsome URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include,re_path
from django.contrib import admin
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('buy12', views.buy12, name='buy12' ),
    path("sign12", views.sign12, name="sign12"),
    path("login12", views.login12, name="login12"),
    path('faq', views.faq, name='faq' ),
    path('vet', views.vets, name='vets' ),
    path('PetList', views.PetList, name='PetList' ),
    path('contact', views.contact, name='contact' ),
    path('PetProductList', views.PetProductList, name='PetProductList' ),
    path('DayCare', views.DayCare, name='DayCare' ),
    path('Caretaker', views.Caretaker, name='Caretaker' ),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path('products/contact', views.contact, name='contact' ),
    path('checkout', views.checkout, name='checkout' ),
    path("handlerequest/", views.handlerequest, name="HandleRequest"),
    path('chatbot/', views.chatbot, name='chatbot'),
    path('bot_search/', views.bot_search, name='bot_search'),
    path('pets/<int:myid>', views.contactbreeder, name='contactbreeder' ),
    path('pets/contact', views.contact, name='contact'),
    path("caretaker/<int:myid>", views.cportal, name="cportal"),
    path('cportal', views.cportal, name='cportal'),
    path('customer-deals', views.customerdeals, name='customer-deals' ),
    path("caretakersignup", views.caretakersignup, name="caretakersignup"),
    path("caretakerlogin",views.caretakerlogin, name="caretakerlogin"),
    path("caretakerlogout",views.caretakerlogout,name="caretakerlogout")

]
