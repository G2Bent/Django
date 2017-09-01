from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Question,Choice
from django.http import HttpResponse
import json
# Create your views here.
def index(request):
    latest_question_list = Question.objects.all()
    dicts = { }
    if latest_question_list:
        for question in latest_question_list:
            dicts[question.id] = question.question_text
        j = json.dumps(dicts)
        return HttpResponse(j)
    else:
        return HttpResponse("question list null")
    #context = {'latest_question_list':latest_question_list}
    #return render(request,'polls/index.html',context)

#查看单个问题选项
def detail(request,question_id):
    choices = Choice.objects.filter(question_id = question_id)
    dicts = { }
    print(question_id)
    if question_id:
        for choice in choices:
            dicts[choices.id] = choice.choice_text
        j = json.dumps(dicts)
        return HttpResponse(j)
    #question = get_object_or_404(Question,pk = question_id)
    #return render(request,'polls/detail.html',{'question':question})

#查看投票结果
def results(request,question_id):
    question = get_object_or_404(Question,pk = question_id)
    return render(request,'polls/results.html',{'question':question})

#选择投票
def vote(request,question_id):
    p = get_object_or_404(Question,pk = question_id)
    try:
        selected_choice = p.choice_set.get(pk = request.POST['choice'])
    except(KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',
                      {'question': p,
                        'error_message':'你没有选择！',})
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(p.id,)))