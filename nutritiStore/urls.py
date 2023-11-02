from django.urls import path #3 copy paste fro nutriti and change
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('about/', views.about, name='about'), 
    path('login/', views.login_user, name='login'), 
    path('logout/', views.logout_user, name='logout'), 
]
