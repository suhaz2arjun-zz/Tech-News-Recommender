from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from tech.models import News

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']
class ProfileRegisterForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['interest']
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['image','interest']

class NewsUploadForm(forms.ModelForm):
    class Meta:
        model=News
        fields=['news_id','news_title','news_genre','news_plot','news_link']