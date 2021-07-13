from django.contrib import admin

# Register your models here.
from .models import News,News_Rating
# Register your models here.
admin.site.register(News)
admin.site.register(News_Rating)
