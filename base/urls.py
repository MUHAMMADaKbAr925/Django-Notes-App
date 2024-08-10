from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name="home"),
    path('note/<int:pk>', views.note_view, name='note'),
    path('register/', views.register_view, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),

    path('new/', views.newMessage, name='new'),
    path('delete/<int:pk>', views.deleteMessage, name='delete'),

]
