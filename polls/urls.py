from django.contrib import admin
from django.urls import path

from polls.views import index, detail, detail2, vote, edit, save

urlpatterns = [
    path('', index),
    path('<int:question_id>', detail,name = 'detail'),  # 반드시 숫자입력
    path('<int:num1>/<int:num2>', detail2),  # 반드시 숫자입력
    path('<int:question_id>/vote',vote), # 반드시 숫자입력
    path('<int:question_id>/edit',edit),
    path('<int:question_id>/save',save),

]
