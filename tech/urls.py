from django.urls import path

from .views import *

app_name='tech'

urlpatterns = [
    path('news/',news_home,name='home'),
    path('detail/',news_detail,name='detail'),
    path('about/',about,name='about'),
    path('rate/',rate_show,name='rate'),
    path('',homepage,name='homepage'),

    #path('upload/',upload,name='upload'),
]