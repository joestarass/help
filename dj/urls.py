from django.contrib import admin
from django.urls import path
from Book import views

urlpatterns = [
    path("", views.index),
    path('book/<int:book_id>', views.get_info_404)
]

