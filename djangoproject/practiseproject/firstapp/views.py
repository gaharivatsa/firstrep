from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html',{'name':'P OLL'})

def add(request):
    val1 = request.GET['num1']
    val2 = request.GET['num2']
    res = int(val1) + int(val2)
    return render(request,'result.html',{'res':res})