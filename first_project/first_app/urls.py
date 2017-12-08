from django.urls import path,include
from first_app import views

urlpatterns = [
    path('',views.index,name="index"),
    path('picture/', views.index2,name="index2"),
]