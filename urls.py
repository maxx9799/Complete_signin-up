from django.urls import path
from django.urls.resolvers import URLPattern
from . import views # . -> pwd

app_name = "users"   



urlpatterns = [
    path("", views.index),
    # path("home/", views.home),
    path("signin/", views.signin),
    # path("afterlogin/", views.afterlogin),
    path("register/", views.register),#bydefault search func for that name so write as_view for the class
    path("aftersignup/", views.aftersignup.as_view()),
    path("aftersignin/", views.aftersignin.as_view()),
    path("details/", views.details),
    path("edit/<int:id>", views.edit, name = "edit"),
    path("delete/<int:id>", views.delete, name = "delete"),
    path("logout/", views.logout, name = "logout"),
]

