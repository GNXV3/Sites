from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('leagues/', views.leagues, name='leagues'),
    path('teams/', views.teams, name='teams'),
    path('about/', views.about, name='about'),
]