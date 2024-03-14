from django.shortcuts import render
from .models import Rubric

# Create your views here.

def test(request):
    rubrics = Rubric.objects.all()
    return render(request, "testapp/test.html", {'rubrics': rubrics})