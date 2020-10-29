from django.urls import path
from .views import *

urlpatterns = [
    path('', index,name='index'),
    path('subview/<str:pk>/',SubjectView,name='subview'),
    path('chapter_view/<str:pk>/',ChapterView,name='chapter_view'),
    path('author_view/<str:pk>', AuthorView,name='author_view'),
    path('doubt',Doubt,name='doubt'),
    path('answer',AnswerView,name='answer'),
]