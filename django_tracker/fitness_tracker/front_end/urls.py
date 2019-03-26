from django.urls import path
from . import views

urlpatterns = [
    path('index.html',views.home,name='home-link'),
    path('about.html',views.about,name='about-link'),
    path('about/',views.about,name='front_end-about'),
    path('', views.home, name='front_end-default'),
    path('home/',views.home,name='front_end-home'),
    path('home',views.home,name='home'),
]
