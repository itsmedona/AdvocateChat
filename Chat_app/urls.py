from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('<str:room>/', views.room, name="room"),
    path('checkview/', views.checkview, name="checkview"),
    path('user_home', views.user_home, name="user_home"),
    path('user_room/<str:user_room>/<str:username>', views.user_room, name="user_room"),
    path('user_checkview', views.user_checkview, name="user_checkview"),
    path('send/', views.send, name="send"),
    path('getMessages/<str:room>/', views.getMessages, name="getMessages")
]