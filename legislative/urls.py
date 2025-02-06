from django.urls import path
from . import views

app_name = 'legislative'

urlpatterns = [
    path('', views.home, name='home'),
] 