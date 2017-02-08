from django.shortcuts import render
from django.http import HttpResponse
import requests
from my_app.models import Question
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def base(request):
    return render(request, 'my_app/base.html')

@csrf_exempt
def home(request):
    context = {}
    if request.method == 'POST':
        answer = request.POST['question']
        q = Question(question_text=answer , pub_date = '2017-02-05 17:10')
        q.save()
        context = {'question': q}

    else:
        entry = Question.objects.all()
        context = {'entry': entry}
    return render(request, 'my_app/home.html', context)
    #return HttpResponse("Hello, world. You're at the my_app index.")

def index(request):
    context = {'ash': 'ashley'}
    return render(request, 'my_app/index.html', context)
