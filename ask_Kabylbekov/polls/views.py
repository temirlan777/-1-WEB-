from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.template import Context
from polls.models import CustomUser, Tag, Like, Question, Answer


def listing(request, object_list, NumPerOnePage):
    paginator = Paginator(object_list, NumPerOnePage) 
    page = request.GET.get('page')
    try:
        PAGE = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        PAGE = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        PAGE = paginator.page(paginator.num_pages)

    return PAGE

Tag_List = Tag.objects.all()
context = {'tags' : Tag_List}

def NewQuestions(request):
    NewQuestions_ = Question.newest_questions.all()
    page =  listing(request, NewQuestions_, 3)
    context.update({'questions': page})
    return render_to_response('index.html',  context )

def Signup(request):
    return render_to_response('signup.html', context)

def Login(request):
    return render_to_response('login.html', context)

def OneQuestion(request, question_id):
    OneQuestion_ = Question.objects.get(pk = question_id)
    Answers = OneQuestion_.answer_set.order_by('-created')
    page =  listing(request, Answers, 3)
    context.update( { 'question': OneQuestion_, 'answers': page } ) 
    return render_to_response('question.html', context)

def Ask(request):
    return render_to_response('ask.html', context)

def BestQuestions(request):
    BestQuestions_ = Question.best_questions.all()
    page =  listing(request, BestQuestions_, 3)
    context.update ( {'questions': page } )
    return render_to_response('index.html',  context )

def TagsQuestions(request, tag):
    TagsQuestions_ = Question.newest_questions.filter(tags__title__exact = tag)
    page =  listing(request, TagsQuestions_, 3)
    context.update({'questions': page })
    return render_to_response('index.html', context)


"""
#Home work N = 2
def hello(request):
    return HttpResponse(["Hello world"])

from django.template.loader import get_template 
from django.template import Context

def params(request):
    body = 'Hello, world!<br>'

    body += '<br>Method: ' + request.method + '<br>'
    if request.method == "GET":
        body += '<br>Params1:<br>' + parse_query_string(request.GET.urlencode())
    if request.method == "POST":
        body += '<br>Params1:<br>' + parse_query_string(request.POST.urlencode())
    return HttpResponse([ body ])

def parse_query_string(query_string):
    query_string_array = query_string.split('&')
    query_string = ''
    for param in query_string_array:
        query_string += param + '<br>'
    return query_string

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def first(request):
    view = "Hi!"
    return render_to_response('base.html', {})
    t = get_template('base.html')
    return HttpResponse(t)"""