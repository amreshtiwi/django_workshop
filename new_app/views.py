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
    trip1 = trip()
    trip1.name = 'Mumbai'
    trip1.descrption = 'The city that never sleeps'
    trip1.image = 'destination_1.jpg'
    trip1.price = 120

    trip2 = trip()
    trip2.name = 'Mumbai'
    trip2.descrption = 'The city that never sleeps'
    trip2.image = 'destination_2.jpg'
    trip2.price = 120

    trip3 = trip()
    trip3.name = 'Mumbai'
    trip3.descrption = 'The city that never sleeps'
    trip3.image = 'destination_3.jpg'
    trip3.price = 120

    trips = [trip1,trip2,trip3]
    return render(request, "index.html" ,{'trips':trips})