from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, request
from django.template import loader
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Question,Choice
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from . import forms
from .forms import FormVote,FormAddChoice,FormName

#version 1
# def index(request):
#     # return HttpResponse("Hello, world. You're at the polls index.")
#     latest_list=Question.objects.order_by('-pub_date')[:5]
#     lastest_question_list={'lastest_question_list':latest_list}
#     return render(request,"polls/index.html",context=lastest_question_list)
#
# def detail(request,question_id):
#     # return HttpResponse("You are looking at the question %s"%question_id)
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
#
#
#
# def results(request,question_id):
#     # response="You are looking at the results of the question %s"
#     # return HttpResponse(response %question_id)
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = 'lastest_question_list'

    def get_queryset(self):
        # return Question.objects.order_by('-pub_date')[:5]

        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

        """Question.objects.filter(pub_date__lte=timezone.now()) returns a queryset 
        containing Questions whose pub_date is less than or equal to - that is, 
        earlier than or equal to - timezone.now."""

class IndexView2(generic.ListView):
    template_name = "polls/index2.html"
    context_object_name = 'lastest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('pub_date')[:3]



# def addChoice(request):
#     form1 = forms.FormAddChoice()
#     if request.method == 'POST':
#         form1 = forms.FormAddChoice(request.POST)
#
#     if form1.is_valid():
#         print('SUCCESS!')
#         form1.cleaned_data['choice_content']
#
#     return render(request, 'polls/addQuestion.html', {'formAddChoice': form1})

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'



#     return render(request,'polls/addQuestion.html')

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


class AllQuestion(generic.ListView):
    template_name = "polls/allQuestion.html"
    context_object_name = 'question_list'

    def get_queryset(self):
        return Question.objects.order_by('pub_date')
    # question=Question.objects.all()
    # return render(request,'polls/allQuestion.html',{'question_list':question})


#+++++++++++++++++++++++++++++++++==

# def vote(request,question_id):
#     # return HttpResponse("You are voting on the question %s"%question_id)
#     question=get_object_or_404(Question,pk=question_id)
#     try:
#         selected=question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError,Choice.DoesNotExist):
#         return render(request,"polls/detail.html",{
#             'question':question,
#             'error_message':"You did not select a choice",
#         })
#     else:
#         selected.votes+=1
#         selected.save()
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
# # Create your views here.


def addQuestion(request):

    if request.method == 'POST':
        form =FormName(request.POST)

        if form.is_valid():
            content = form.cleaned_data['question_content']
            if content:
                question = Question.objects.create(question_text=content,pub_date=timezone.now())

            # redirect to a new URL:
                return render(request,'polls/success.html',{'pre_link':'/polls'})
            else:
                return render(request, 'polls/addQuestion.html', {'error_message':"Fail to add new one!"})

    else:
        form = forms.FormName()
        return render(request,'polls/addQuestion.html',{'form':form})

# def doAddQuestion(request):
#     # form =forms.FormName()
#     if request.method == 'POST':
#         form =forms.FormName(request.POST)
#
#         if form.is_valid():
#             content = form.cleaned_data['question_content']
#             question = Question.objects.create(question_text=content,pub_date=timezone.now())
#
#             # redirect to a new URL:
#             return HttpResponseRedirect(reverse('polls:success'))
#     return render(request, 'polls/addQuestion.html', {'error_message':"Fail to add new one!"})

# def form_add_question_view(request):
#     form = forms.FormName()
#     return render(request,'polls/addQuestion.html',{'form':form})

def success(request):
    return render(request,'polls/success.html')

def vote(request,question_id):

    c=Choice.objects.filter(question_id=question_id)
    question_obj=Question.objects.get(id=question_id)
    template = loader.get_template('polls/votes.html')

    if request.method == 'POST':
        formVote = FormVote(request.POST,question_id=question_id)
        formAddChoice = FormAddChoice(request.POST)

        if formAddChoice.is_valid():
            content= formAddChoice.cleaned_data['choice_content']
            c = Question.objects.get(pk=question_id)
            c.choice_set.create(choice_text=content, votes=0)

            # redirect to a new URL:
            return render(request,'polls/success.html',{'pre_link':'/polls/'+str(question_id)+'/vote'})
        if formVote.is_valid():
            choice = formVote.cleaned_data['votes']
            if choice:
                choice.votes+=1
                choice.save()
                return render(request,'polls/results.html',{'question':question_obj,'pre_link':'/polls/'+str(question_id)+'/vote'})
            else:
                return render(request,'polls/error.html')


    # return render(request, 'polls/test.html', {'test': question_id})
    # return render(request, 'polls/votes.html', {'formVote': formVote,'formAddChoice':formAddChoice})

    formVote = forms.FormVote(question_id=question_id)
    formAddChoice = forms.FormAddChoice()
    context = {
        'question_obj': question_obj,
        'choices': c,
        'formVote': formVote,
        'formAddChoice': formAddChoice,
    }
    return HttpResponse(template.render(context, request))