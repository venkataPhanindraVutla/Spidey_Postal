from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"), 
    path("stamps/", views.stamps, name="stamps"),
    path("login/",views.login,name='login'),
]
