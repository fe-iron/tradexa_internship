from .views import index, post_create
from django.urls import path


urlpatterns = [
    path('', index, name="index"),
    path('post_create', post_create, name="post_create"),

]