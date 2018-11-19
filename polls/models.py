from django.db import models

# Create your models here.
class Question(models.Model): # 질문
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text
    # 내가 집어넣은 데이터를 보기 쉽게 하기 위해 . 질문
class Choice(models.Model): # 보기
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # ForignKey를 가지고 있는 Choice가 하나의 노예,question=주인
    # on_delete 꼭 사용해야하는 것이 아님. 질문이 삭제 되었을때 보기도 같이 삭제
    # on_delete라는 비슷한것이 3가지가 있다.
    # 1.set_null,on_deleteq
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # 질문과 보기를 같이사용.

    def __str__(self):
        return self.choice_text
    # 내가 집어넣은 데이터를 보기 쉽게 하기 위해 . 보기
