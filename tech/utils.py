#!/usr/bin/env python
# coding: utf-8
import pandas as pd
from rake_nltk import Rake
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from surprise import Reader, Dataset, SVD
from surprise.model_selection import cross_validate
import os
from accounts.models import Profile
from .models import *

data_path=os.path.abspath('test_data.csv')
rating_path=os.path.abspath('test_ratings.csv')

def get_news_details(title):
    qSet=News.objects.filter(news_title=title)
    qSet=qSet[0]
    #print(qSet)
    ans={}
    ans['news_title']=qSet.news_title
    ans['news_id']=qSet.news_id
    ans['news_plot']=qSet.news_plot
    ans['news_genre']=qSet.news_genre
    #ans['news_author']=qSet.news_author
    ans['news_link']=qSet.news_link
    ans['news_rating']=qSet.news_rating
    return ans

def popular_news():
    temp=[]
    obj= News.objects.all()
    for i in obj:
        temp.append([i.news_id,i.news_title,i.news_genre,i.news_plot,i.news_link,i.news_rating])
    temp.sort(key= lambda x:x[-1],reverse=True)
    ans = []
    i = 0
    for row in temp:
        if (i < 3):
            ans.append(row[1])
            i+=1
    final=[]
    for j in ans:
        final.append(get_news_details(j))
    return final

def top_charts(genre):
    temp=[]
    obj= News.objects.all()
    for i in obj:
        temp.append([i.news_id,i.news_title,i.news_genre,i.news_plot,i.news_link,i.news_rating])
    # temp.sort(key= lambda x:x[-1],reverse=True)
    #data = data.sort(data.news_rating, ascending=False)
    ans = []
    for row in temp:
        if (genre in row[2]):
            ans.append(row[1])
    final=[]
    for i in ans:
        final.append(get_news_details(i))
    return final


def clean_genre(s):
    return s.replace(' ', '').split(',')


def similar_shows(title, request):
    temp=[]
    obj= News.objects.all()
    for i in obj:
        temp.append([i.news_id,i.news_title,i.news_genre,i.news_plot,i.news_link,i.news_rating])
    temp.sort(key= lambda x:x[-1],reverse=True)
    data= pd.DataFrame(temp, columns =['news_id', 'news_title','news_genre','news_plot','news_link','news_rating'])
    data['news_genre'] = data['news_genre'].map(lambda x: clean_genre(x))
    data['key_words'] = ""

    for index, row in data.iterrows():
        plot = row['news_plot']
        r = Rake()

        r.extract_keywords_from_text(plot)

        key_words_dict_scores = r.get_word_degrees()
        data.at[index, 'key_words'] = list(key_words_dict_scores.keys())
    data.drop(columns=['news_plot'], inplace=True)
    data.set_index('news_title', inplace=True)
    data['bag_of_words'] = ''
    columns = data.columns
    for index, row in data.iterrows():
        words = ''
        for col in columns:
            words = words + ' '.join(row[col]) + ' '
        data.at[index, 'bag_of_words'] = words

    data.drop(columns=[col for col in data.columns if col != 'bag_of_words'], inplace=True)
    count = TfidfVectorizer()
    count_matrix = count.fit_transform(data['bag_of_words'])
    indices = pd.Series(data.index)
    cosine_sim = cosine_similarity(count_matrix, count_matrix)
    idx = indices[indices == title].index[0]
    score_series = pd.Series(cosine_sim[idx]).sort_values(ascending=False)
    top_10_indexes = list(score_series.iloc[0:4].index)
    ans=[]
    for i in top_10_indexes:
        ans.append(data.iloc[i].name)
    final=[]
    for i in ans:
        final.append(get_news_details(i))
    return final
            # data = pd.read_csv(rating_path)
            # combine_post_rating = data.dropna(axis = 0, subset = ['news_title'])

            # post_ratingCount = (combine_post_rating.groupby(by = ['news_title'])['rating'].
            #  sum().
            # reset_index().
            # rename(columns = {'rating': 'totalratings'})
            #  [['news_title', 'totalratings']]
            # )
            # totalValuableCount = combine_post_rating.merge(post_ratingCount, left_on = 'news_title', right_on = 'news_title', how = 'left')
            # from scipy.sparse import csr_matrix
            # rating_popular_post_pivot = totalValuableCount.pivot(index = 'news_title', columns = 'username', values = 'totalratings').fillna(0)
            # rating_popular_post_matrix = csr_matrix(rating_popular_post_pivot.values)
            # from sklearn.neighbors import NearestNeighbors
            # model_knn = NearestNeighbors(metric = 'cosine', algorithm = 'brute')
            # model_knn.fit(rating_popular_post_matrix)
            # import numpy as np
            # length=len(rating_popular_post_pivot)
            # for i in range(0,length):
            #     if title==rating_popular_post_pivot.index[i]:
            #         query_index = i
            #         distances, indices = model_knn.kneighbors(rating_popular_post_pivot.iloc[query_index,:].values.reshape(1, -1), n_neighbors = 6)
            #         break
            #     else:
            #         query_index = np.random.choice(rating_popular_post_pivot.shape[0])
            #         distances, indices = model_knn.kneighbors(rating_popular_post_pivot.iloc[query_index,:].values.reshape(1, -1), n_neighbors = 2)
            # ans=[]  
            # for i in range(1, len(distances.flatten())):
            #     ans.append(rating_popular_post_pivot.index[indices.flatten()[i]])
            # final=[]
            # for i in ans:
            #     final.append(get_news_details(i))
            # return final


def personalized_shows(username,request):
    obj= Profile.objects.filter(user=request.user).first()
    dominelist=obj.interest
    ratings = pd.read_csv(rating_path)
    reader = Reader()
    data = Dataset.load_from_df(ratings[['username', 'news_title', 'rating']], reader)
    #data.split(n_folds=10)
    svd = SVD()
    cross_validate(svd, data, measures=['RMSE'],cv=2)
    temp=[]
    obj=News.objects.all()
    for i in obj:
        if i.news_genre in dominelist:
                temp.append([i.news_id,i.news_title,svd.predict(username,i.news_title).est])
        temp.sort(key= lambda x:x[2],reverse=True)
    ans=[]
    rated=News_Rating.objects.filter(username=username)
    already_rated=[]
    for i in rated:
        already_rated.append(i.news_title)
    j=0
    for i in temp:
        if(j>5):
            break
        if(i[0] not in already_rated):
            ans.append(i[1])
            j+=1

    final=[]
    for i in ans:
        final.append(get_news_details(i))
    return final

def rate_show(username,news_title,rating):
    qSet=News_Rating.objects.filter(username=username,news_title=news_title)
    if(len(qSet)==0):
        old = open(rating_path,'a')
        old.write(str(username) + "," + str(news_title) + "," + str(rating) + "\n")
        old.close()
        obj = News_Rating(username=str(username), news_title=str(news_title), rating=str(rating))
        obj.save()
    else:
        #to update rating csv file
        qSet[0].rating=rating
        qSet[0].save()
        with open(rating_path, 'r') as f:
            data = f.readlines()
            f.close()
        for i in range(len(data)):
            if ((username + ',' + news_title) in data[i]):
                data[i] = username + ',' + news_title + ',' + rating+'\n'
        with open(rating_path, 'w') as file:
            file.writelines(data)
            file.close()