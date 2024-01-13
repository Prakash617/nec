from django.urls import path,include
from .views import *

urlpatterns = [
    
    path('quiz_home', quiz_home, name="quiz_home"),
    path('addQuestion/', addQuestion,name='addQuestion'),
    path('sub_title_quiz/<str:sub_category>', sub_title_quiz,name='sub_title_quiz'),
    # path('results', quiz_results, name="quiz_results"),
    # path('slogin', superuser_login, name="slogin"),
    # path('superuser/logout', superuser_logout, name="superuser_logout"),
    # path('feed', feed, name="feed"),
    
    # # path('nec', nec_page, name="nec_page"),
    # path('<str:course_name>/', course, name='course'),
    # path('<str:course_name>/<str:sub_category>/', course_detail, name='course_detail'),


    
]
