from django.urls import path, include
from . import views
from django.conf import settings

urlpatterns = [
    path("user", views.getUser),
    # path('user/post', views.postUser)
]
