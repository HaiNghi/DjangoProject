from django.contrib import admin
from django.urls import path, include
from boards import views

urlpatterns = [
    # path('<int:pk>/',views.board_topics,name="board_topics"),
    path('<int:pk>/',views.TopicListView.as_view(),name="board_topics"),
    path('<int:pk>/new/',views.new_topic, name="new_topic"),
    path('<int:pk>/topics/<int:topic_pk>/',views.PostListView.as_view(),name="topic_posts"),
    path('<int:pk>/topics/<int:topic_pk>/reply/', views.reply_topic, name="reply_topic"),
    path('<int:pk>/topics/<int:topic_pk>/posts/<int:post_pk>/edit/',views.PostUpdateView.as_view(),name='edit_post'),
]