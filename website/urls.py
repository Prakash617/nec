from django.urls import path,include
from .views import *

urlpatterns = [
    
    path('', home, name="admin_page"),
    path('superuser', superuser, name="superuser"),
    path('slogin', superuser_login, name="slogin"),
    path('superuser/logout', superuser_logout, name="superuser_logout"),
    path('feed', feed, name="feed"),
    
    # path('nec', nec_page, name="nec_page"),
    path('course/<str:course_name>/', course, name='course'),
    path('course/<str:course_name>/<str:sub_category>/', course_detail, name='course_detail'),


    
]
