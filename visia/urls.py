from django.urls import path

from visia import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('register', views.register, name='register'),
    path('addUser', views.addUser, name='addUser'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('otpGenerate', views.otpGenerate, name='otpGenerate'),



]
