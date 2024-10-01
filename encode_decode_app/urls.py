from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('code/', views.decode_message, name='decode_message'),
]
