from django.urls import path
from . import views_users

urlpatterns = [
    path('login/',views_users.v_login, name="Login"),
    path('signin/',views_users.v_signin, name="Signin"),
    path('profile/',views_users.v_profile, name="Profile"),
    path('friends/',views_users.v_profile, name="Friends"),
    path('logout/',views_users.v_logout, name="Logout"),

]