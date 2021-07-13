from django.shortcuts import render,redirect
from django.http import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth import login
from django.contrib.auth import logout
from .models import Profile
from django.contrib.admin.views.decorators import staff_member_required
from .forms import ProfileRegisterForm, ProfileUpdateForm,UserRegisterForm,NewsUploadForm

def logout_view(request):
    logout(request)
def login_view(request):
    login(request)

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, ProfileRegisterForm
class MySignUpView(View):
    form_class = UserRegisterForm
    # form_class = UserCreationForm
    template_name = 'accounts/sign_up.html'
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            # <process form cleaned data>
            u = User.objects.create_user(
                    username=form.cleaned_data.get('username'),
                    password=form.cleaned_data.get('password1'),
                    email=form.cleaned_data.get('email'),
                    is_active = True
            )
            login(request,u)
            
            # TODO Display message and redirect to login
            return HttpResponseRedirect('/accounts/interest')
        return render(request, self.template_name, {'form': form})

# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(
#                 request, f'Your account has been created!You are now able to login.')
#             return redirect('accounts:interest')
#     else:
#         form = UserRegisterForm()
#     context={
#         'form':form
#     }
#     return render(request, 'accounts/sign_up.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        u_form =UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST, request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(
            request, f'updated sucessfully')
            return redirect('accounts:profile')
    else:
        u_form =UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)
    context={
        'u_form': u_form,
        'p_form':p_form
    }


    return render(request, 'accounts/profile.html', context)

def interest(request):
    if request.method == 'POST':
        pr_form=ProfileRegisterForm(request.POST, request.FILES,instance=request.user.profile)
        if pr_form.is_valid():
            pr_form.save()
            messages.success(
                request, f'interests stored sucessfully'
            )
            return redirect('news_home')
    else:
        pr_form=ProfileRegisterForm(instance=request.user.profile)
    context={
        'pr_form':pr_form
    }
    return render(request, 'accounts/interest.html', context)

@staff_member_required
def news_upload(request):
    if request.method == 'POST':
        n_form=NewsUploadForm(request.POST)
        if n_form.is_valid():
            n_form.save()
            messages.success(
                request, f'Post uploaded successfully'
            )
            return redirect('news_home')
    else:
        n_form=NewsUploadForm()
    context={
        'n_form':n_form
    }
    return render(request, 'accounts/news_upload.html', context)