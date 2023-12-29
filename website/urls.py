from django.urls import path,include
from .views import *

urlpatterns = [
    
    path('', home, name="admin_page"),
    path('superuser', superuser, name="superuser"),
    path('slogin', superuser_login, name="slogin"),
    # path('nec', nec_page, name="nec_page"),
    path('<str:course_name>/', course, name='course'),

    path('superuser/logout', superuser_logout, name="superuser_logout"),

    
]
