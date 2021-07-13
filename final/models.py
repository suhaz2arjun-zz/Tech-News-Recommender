from django.db import models

# Create your models here.
class News(models.Model):
    news_id=models.CharField(max_length=10)
    news_title=models.CharField(max_length=100)
    news_genre=models.CharField(max_length=100)
    news_plot=models.CharField(max_length=2000)
    #news_author=models.CharField(max_length=100)
    news_link=models.CharField(max_length=200)
    news_rating=models.CharField(max_length=100)

    def __str__(self):
        return self.news_title

class News_Rating(models.Model):
    username = models.CharField(max_length=100)
    news_title = models.CharField(max_length=100)
    rating=models.FloatField()
