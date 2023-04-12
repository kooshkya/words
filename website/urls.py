from django.urls import path, re_path

from . import views

app_name = "website"
urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register_user, name="register"),
    path("add_word/", views.add_word, name="add_word"),
    path("delete_word/<int:pk>/", views.delete_word, name="delete_word"),
]
