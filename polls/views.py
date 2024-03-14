from django.shortcuts import render
from .models import Poll

# Create your views here.

def index(request):
    polls = Poll.objects.all()
    return render(request, 'polls/index.html', {'polls':polls})

def detail(request, id):
    poll = Poll.objects.get(id=id)
    return render(request, 'polls/detail.html', {'poll':poll})
