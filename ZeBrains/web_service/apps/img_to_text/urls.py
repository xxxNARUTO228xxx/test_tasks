from django.urls import path

from . import views

urlpatterns = [
    path('', views.im2text, name="home"),
]
