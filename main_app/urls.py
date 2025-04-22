from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #will hold all the routes here
    path('about/', views.about, name='about'),
    path('cats/', views.cat_index, name='cat_index'),

]

