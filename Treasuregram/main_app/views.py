from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>The science is just to keep spinning <br>because the big bang is only just beginning <br> and sometimes it is all that we can do <br> just to hang on</h1>')