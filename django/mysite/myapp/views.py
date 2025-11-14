from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello(request):
    try:
        return render(request, 'hello.html')
    except Exception as e:
        return HttpResponse(str(e))