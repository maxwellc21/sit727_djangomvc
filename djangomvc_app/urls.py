from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/message/', views.get_message, name='get_message'),
]