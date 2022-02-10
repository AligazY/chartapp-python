from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pie/', views.pie, name='pie'),
    path('line/', views.line, name='line'),
]
