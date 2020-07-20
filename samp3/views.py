from django.shortcuts import render
from django.http import HttpResponse

def home(request):
  return HttpResponse("<h1>'WELCOME TO MY HOMEPAGE'</h1>")

def sample1(request):
  return render(request,"sample1.html")

def sample2(request):
  return render(request,"directory\sample2.html")