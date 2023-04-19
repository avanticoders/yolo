from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add-task/', views.add_task, name="add-task"),
    path('delete-task/<int:pk>', views.delete_task, name="delete-task"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('signin/', views.signin_user, name="signin"),
]