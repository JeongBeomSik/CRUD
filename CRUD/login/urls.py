
from django.contrib import admin
from django.urls import path, include
import base.views
import login.views

urlpatterns = [
    path('', login.views.login, name="login"),
    path('signup/',login.views.signup, name="signup"),
    path('create/',login.views.create, name="create"),
    path('signin/',login.views.signin, name="signin"),
    path('logout/',login.views.logout, name="logout"),
    path('profile_update/',login.views.profile_update, name="profile_update"),
    path('update_profile/',login.views.update_profile, name="update_profile"),


]
