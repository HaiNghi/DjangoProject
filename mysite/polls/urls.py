from django.urls import path
from . import views


#version1
# urlpatterns=[
#     path('',views.index,name="index"),
#     path('<int:question_id>/',views.detail,name="detail"),
#     path('<int:question_id>/results/', views.results, name="results"),
#     path('<int:question_id>/vote/',views.vote,name="vote"),
#
# ]

from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('top3/',views.IndexView2.as_view(),name='index2'),
    path('add/',views.addQuestion, name='addQuestion'),
    # path('add/doAdd/',views.doAddQuestion,name='doAddQuestion'),
    path('add/success/',views.success, name='success'),
    path('show/',views.AllQuestion.as_view(), name="allQuestion"),
]