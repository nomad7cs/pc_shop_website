from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pc_details/', views.pc_details, name='pc_details'),
    path('', views.index, name='index'),
    path('', views.index, name='index'),
    path('', views.index, name='index'),
    path('', views.index, name='index'),
    path('', views.index, name='index'),
]