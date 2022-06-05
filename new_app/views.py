from django.http.response import HttpResponse
from django.shortcuts import render
from .models import trip

# Create your views here.
def home(request):
    #return HttpResponse("<h1>Hello world!</h1>")
    return render(request , 'home.html',{'name':'Amoora'})

def add(request):
    val1 =int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    res=val1+val2
    return render(request,"result.html",{'result': res})

def index(request):
    trips=trip.objects.all()
    return render(request, "index.html" ,{'trips':trips})