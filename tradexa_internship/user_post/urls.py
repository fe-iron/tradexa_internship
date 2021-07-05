from .views import index, register, login, logout
from django.urls import path


urlpatterns = [
    path('', index, name="create-post"),
    path('register', register, name="register"),
    path('login', login, name="login"),
    path('logout', logout, name="logout"),
]