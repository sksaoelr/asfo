from django.urls import path
from .views import base_views, question_views, answer_views, category_views

app_name = 'asfo'

urlpatterns = [
    # base_views.py
    path('',
         base_views.index, name='index'),
    path('<int:question_id>/',
         base_views.detail, name='detail'),

    path('main',
         base_views.main, name='main'),

    path('item_list',
         category_views.item_list, name='item_list'),

    # question_views.py
    path('question/create/',
         question_views.question_create, name='question_create'),

    # answer_views.py
    path('answer/create/<int:question_id>/',
         answer_views.answer_create, name='answer_create')
]