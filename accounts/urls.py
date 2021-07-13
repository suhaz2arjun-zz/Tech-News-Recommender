from django.urls import path,include
from django.contrib.auth.views import (
    LoginView, LogoutView,)
from .views import *
from tech.views import news_home
# from django.conf import settings
# from django.conf.urls.static import static
app_name = 'accounts'
urlpatterns = [
    # path('register/', register, name='register'),
    path('sign_up/', MySignUpView.as_view(), name='sign_up'),
    path('profile/', profile, name='profile'),
    path('interest/', interest, name='interest'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name="login"),
    path('news_upload/', news_upload, name='news_upload'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name="logout"),
    path('',news_home,name='news_home'),
    # path('',include('new.urls')),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)