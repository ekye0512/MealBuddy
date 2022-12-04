from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('customer/', views.customer),
    path('dashboard/', views.dash),

]