from django.urls import path

from . import views

urlpatterns = [
    path('', views.text2emo, name="home"),
]
