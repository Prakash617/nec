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
    
    path('courses', courses_list.as_view(), name="courses_list"),
    path('subjects/<str:subject_name>', subjects.as_view(), name="subjects"),
    # path('courses_list', , name="courses_list"),
    
    path('course/<str:course_name>/', course, name='course'),
    path('course/<str:course_name>/<str:sub_category>/', course_detail, name='course_detail'),


    
]
