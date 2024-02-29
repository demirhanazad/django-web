from django.urls import path
from . import views


urlpatterns = [
    path("login",views.giris,name="login"),
    path("register",views.register,name="register"),
    path("",views.logout_request,name="logout"),
]
