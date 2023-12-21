from django.urls import path,include
from .views import *

urlpatterns = [
    
    path('', home, name="admin_page"),
    path('superuser', admin_page, name="admin_page"),
    path('slogin', superuser_login, name="superuser_login"),
    path('superuser/logout', superuser_logout, name="superuser_logout"),

    
]
