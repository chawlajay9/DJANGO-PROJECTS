from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from .view.index import Index
from .view.signup import Signup
from .view.login import Login, logout


urlpatterns = [
    path("", Index.as_view()),
    path("signup", Signup.as_view()),
    path("login", Login.as_view()),
    path("logout", logout),
]
