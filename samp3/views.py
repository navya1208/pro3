from django.shortcuts import render
from django.http import HttpResponse

def home(request):
  return HttpResponse("<h1>'WELCOME TO MY HOMEPAGE'</h1>")

def sample1(request):
  return render(request,"sample1.html")

def sample2(request):
  return render(request,"directory\sample2.html", context={'name':'Navya','course':'Python fullstack'})

def sample3(request):
  fruits=['banana','apple','orange','grapes','guava','watermelon']
  return render(request,"directory\sample3.html", context={'fruits':fruits})

def sample4(request):
  a=45;
  b=35;
  sum=a+b
  sub=a-b
  mul=a*b
  div=a//b

  # return render(request,"directory\sample4.html", context={'a':30,'b':45})
  return render(request,"directory\sample4.html",context={'a':a,'b':b,'sum':sum,'sub':sub,'mul':mul,'div':div})

# def great(request,abc):
#   s=list(map(int,abc.split(" ")))
#   return HttpResponse(max(s))

def great(request,a,b,c):
  return HttpResponse(max(a,b,c))

def add(request,ab):
  s=list(map(int,ab.split(" ")))
  Sum=sum(s)
  return HttpResponse(Sum)

def name(request,Name):
  return HttpResponse("<center><h1>My name is {}!!!</h1></center>".format(Name))
