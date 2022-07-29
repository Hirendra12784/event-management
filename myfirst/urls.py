from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('insert',views.insert,name='insert'),
    path('likePost/',views.likePost,name='likePost'),
    path('date',views.date,name='date'),
    path('type',views.type,name='type'),
]