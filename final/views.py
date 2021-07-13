# from tech.models import News_Rating
# from tech.models import News
# from django.shortcuts import render
# from django.contrib import messages
# import csv,io
# from django.contrib.auth.decorators import login_required

# @login_required
# def upload(request):
#     template="final/upload.html"
#     prompt={
#        'order': 'should in order'
#     }
#     if request.method =="GET":
#         return render(request,template,prompt)
#     csv_file= request.FILES['file']
#     if not csv_file.name.endswith('.csv'):
#         messages.error(request,'not csv file')
#     dataset=csv_file.read().decode('UTF-8')
#     io_string=io.StringIO(dataset)
#     next(io_string)
#     for columns in csv.reader(io_string,delimiter=',',quotechar='|'):
#         _, created=News.objects.update_or_create(
#             news_id=columns[0],
#             news_title=columns[1],
#             news_genre=columns[2],
#             news_plot=columns[3],
#             #news_author=columns[4],
#             news_link=columns[4],
#             news_rating=columns[5]
#         )
#     context={}
#     return render(request, template, context) 



# @login_required
# def upload(request):
#     template="final/upload.html"
#     prompt={
#        'order': 'should in order'
#     }
#     if request.method =="GET":
#         return render(request,template,prompt)
#     csv_file= request.FILES['file']
#     if not csv_file.name.endswith('.csv'):
#         messages.error(request,'not csv file')
#     dataset=csv_file.read().decode('UTF-8')
#     io_string=io.StringIO(dataset)
#     next(io_string)
#     for columns in csv.reader(io_string,delimiter=',',quotechar='|'):
#         _, created=News_Rating.objects.update_or_create(
#             username=columns[0],
#             news_title=columns[1],
#             rating=columns[2],
#         )
#     context={}
#     return render(request, template, context) 

from django.http import request
from django.shortcuts import render
from . import utils




