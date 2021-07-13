"""final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from tech.views import news_home,about,homepage
from accounts.views import MySignUpView
from django.contrib.auth import views as auth_views
#from .views import upload

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('tech/', include('tech.urls')),
    path('sign_up/', MySignUpView.as_view(), name='sign_up'),

    #path('',upload,name='upload'),
    path('about/',about,name='about'),
    path('news_home/',news_home,name='news_home'),
    path('',homepage,name='homepage'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="final/password_reset_form.html"),name='reset_password'),
    path('reset_password_sent',auth_views.PasswordResetDoneView.as_view(template_name="final/password_reset_done.html"),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="final/password_reset_confirm.html"),name='password_reset_confirm'),
    path('reset_password_complete',auth_views.PasswordResetCompleteView.as_view(template_name="final/password_reset_complete.html"),name='password_reset_complete'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
