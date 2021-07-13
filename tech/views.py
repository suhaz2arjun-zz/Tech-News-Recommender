from django.shortcuts import render
#import csv,io 
# Create your views here.
from django.http import HttpResponse
#from django.contrib import messages
from . import utils
from .models import News_Rating,News
from accounts.models import Profile
from django.contrib.auth.decorators import login_required



def homepage(request):
    popular_news=utils.popular_news()    
    data={}
    data['popular_news']=popular_news
    return render(request,"tech/home.html",data)

@login_required
def news_home(request):
    data={}
    obj= Profile.objects.filter(user=request.user).first()
    dominelist=obj.interest
    popular_news=utils.popular_news()
    personalized=utils.personalized_shows(str(request.user),request)
    if 'python' in dominelist:
        python=utils.top_charts("python")
        data['python']=python
    if 'ml' in dominelist:
        ml=utils.top_charts("ml")
        data['ml']=ml
    if 'JS' in dominelist:
        JS=utils.top_charts("JS")
        data['JS']=JS
    if 'java' in dominelist:
        java=utils.top_charts("java")
        data['java']=java
    if 'hacking' in dominelist:
        hacking=utils.top_charts("hacking")
        data['hacking']=hacking 
    data['popular_news']=popular_news 
    data['personalized']=personalized
    #TODO render code
    return render(request,'tech/tech.html',data)

def news_detail(request):
    title=request.GET['title']
    news_data=utils.get_news_details(title)
    similar_news=utils.similar_shows(title,request)
    data={}

    data['already_rated'] = False
    data['rating_value'] = 0
    qSet = News_Rating.objects.filter(username=str(request.user))

    for q in qSet:
        if q.news_title == news_data["news_title"]:
            data['already_rated'] = True
            data['rating_value'] = str(q.rating)

    data['news_data']=news_data
    data['similar_news']=similar_news
   

    #TODO render code
    return render(request,'tech/tech_details.html',data)

@login_required
def rate_show(request):
    username=str(request.user)
    news_title=request.GET["news_title"]
    rating=request.GET["rating"]
    utils.rate_show(username,news_title,rating)
    #TODO render code
    return HttpResponse("{'message':'success'}")

@login_required
def about(request):
    data={}
    return render(request,'tech/about.html',data)

