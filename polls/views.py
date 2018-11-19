from django.http import HttpResponse
from django.shortcuts import render

from polls.models import Question

def save(request,question_id):
    q = request.POST['q']
    question = Question.objects.get(id=question_id)
    question.question_text = q
    question.save()

    return HttpResponse('수정 완료')

def edit(request,question_id):
    q = Question.objects.get(id=question_id)

    return render(
        request,'polls/edit.html',{'q':q}
    )
def vote(request,question_id):
    select = request.POST['select']

    q = Question.objects.get(id=question_id)
    c = q.choice_set.get(id=select)
    c.votes += 1
    c.save()
    print(select)
    return render(request,
                  'polls/result.html',
                  {'q':q})
    # return HttpResponse('ok')

def detail(request,question_id):
    q = Question.objects.get(id=question_id) # 조건에 맞는 데이터 하나 조회
    c = q.choice_set.all()
    choice = ''
    # for a in c:
    #    choice += a.choice_text
    # request ,템플릿, 인텍스트(데이터/모델)
    return render(request,'polls/detail.html',{'question':q.question_text,'num': q.id,'choice':c})
    # return HttpResponse(q.question_text+'<br>'+choice)

def detail2(request,num1,num2):
    return HttpResponse(num1+num2)

def index(request):
    questions=Question.objects.all()
    #            request ,     템플릿              컨텍스트 (모듈/데이터)= 만드시 딕셔너리 형태로 사용
    return render(request,'polls/index.html',{'question':questions})
    choices = q.choice_set.all()

    print(q.question_text)
    print(choices[0].choice_text)
    print(choices[1].choice_text)
    print(choices[2].choice_text)

# return HttpResponse('polls index')