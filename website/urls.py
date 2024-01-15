from django.urls import path,include
from .views import *

urlpatterns = [
    
    path('tsignup', signup, name='tsignup'),
    
    path('', home, name="home"),
    path('superuser', superuser, name="superuser"),
    path('slogin', superuser_login, name="slogin"),
    path('login',user_login, name="login"),
    path('signup',user_signup, name="signup"),
    path('superuser/logout', superuser_logout, name="superuser_logout"),
    path('feed', feed, name="feed"),
    
    # path('nec', nec_page, name="nec_page"),
    path('course/<str:course_name>/', course, name='course'),
    path('course/<str:course_name>/<str:sub_category>/', course_detail, name='course_detail'),


    
]
