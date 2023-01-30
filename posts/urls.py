from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
    path("logout", views.logout, name="logout"),
    path("post/<str:id>", views.post, name="post"),
    path("compose", views.compose, name="compose"),
    path("addComment", views.addComment, name="addComment"),
]