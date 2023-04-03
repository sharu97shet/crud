from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from api import views


urlpatterns = [

    path('', views.gethome, name='hethome'),


    # path('account/',   views.register , name='register' ),
]
