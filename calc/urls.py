from django.urls import path, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
from calc import views


urlpatterns = [

    path('', include('visia.urls')),

    path('emp', views.emp, name='emp'),

    path('emppage', views.emppage, name='emppage'),
    path('admin/', admin.site.urls),

    path('api', include('api.urls')),

    path('weather', include('weather.urls')),
    path('indexform', views.indexform),
    path('addstudent', views.addstudent),



    path('sendjson', views.sendjson, name='sendjson'),
    path('addEmployee', views.addEmployee, name='addEmployee'),
    path('rememp', views.rememp, name='rememp'),
    path('rememp/<int:emp_id>', views.rememp, name='rememp'),
    path('viewEmployee', views.viewEmployee, name='viewEmployee'),
    # path('editEmployee/<int:empId>', views.editEmployee, name='editEmployee'),
    path('editEmployee', views.editEmployee, name='editEmployee'),

    path('UPDATE/<int:id>', views.UPDATE, name='editEmployee'),
    path('filter', views.filter, name='filter'),
    path('logoutuser', views.logoutuser, name='logout'),

    path('', views.index, name='index'),
    path('add', views.add, name='add'),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
