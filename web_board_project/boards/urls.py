from django.contrib import admin
from django.urls import path, include
from boards import views

urlpatterns = [
    path('<int:pk>/',views.board_topics,name="board_topics"),
    path('<int:pk>/new/',views.new_topic, name="new_topic"),
]