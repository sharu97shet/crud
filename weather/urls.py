from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='abcd'),
    path('delete/<city_name>/', views.delete_city, name='delete_city'),
]
