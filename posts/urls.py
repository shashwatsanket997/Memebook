from django.contrib.auth import logout
from django.urls import path
from  . import views

urlpatterns = [
    path("", views.getPosts, name="home"),
    path("posts", views.getPosts, name="posts"),
    path("posts/create", views.createPost, name="create-post"),
    path("posts/<int:post_id/detail", views.getPost, name="get-a-post"),
    path("posts/<int:post_id>/edit", views.editPost, name="edit-post"),
    path("posts/<int:post_id>/delete", views.deletePost, name="delete-post"),
    path("posts/<int:post_id>/like", views.likePost, name="like-post"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("register", views.register, name="register"),
     
]
