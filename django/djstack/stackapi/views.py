from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Question
from .serializer import QuestionSerializer
from bs4 import BeautifulSoup
import requests
import json
import datetime
import operator

# Create your views here.

def index(request):
    return HttpResponse("Success")


class QuestionAPI(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

def latest(request):
    try:
        #url = 'https://stackoverflow.com/questions/tagged/android?tab=Newest'
        #data = {'start': '15755763200', 'end': '1575158400'}
        res = requests.get("https://stackoverflow.com/questions/tagged/android?tab=Newest")
        #res = requests.get(url, params=data)
        soup = BeautifulSoup(res.text, "html.parser")

        questions = soup.select(".question-summary")
        for que in questions:
            q = que.select_one('.question-hyperlink').getText()
            vote_count = que.select_one('.vote-count-post').getText()
            views = que.select_one('.views').attrs['title']
            tags = [i.getText() for i in (que.select('.post-tag'))]
            
            question = Question()
            question.question = q
            question.vote_count = vote_count
            question.views = views
            question.tags = tags
            
            
            question.save()
        return HttpResponse("Latest Data Fetched from Stack Overflow")
    except:
        return HttpResponse("Failed")
