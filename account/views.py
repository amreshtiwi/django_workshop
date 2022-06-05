from django.http.response import HttpResponse
from django.shortcuts import render ,redirect
from django.contrib.auth.models import User , auth
from django.contrib import messages
from django.contrib.auth import authenticate
#from .models import trip

# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        username= request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']
        if password == confirmpassword :
            if User.objects.filter(username=username).exists():
                messages.info(request,'User is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.info(request,'Email is taken')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username,email=email,first_name=first_name,last_name=last_name,password=password)
                    user.save()
                    messages.info(request,'Account Created!')
                    return redirect('/')
        else :
            messages.info(request,'Password is not comatable')
            return redirect('register')
    else :
        return render(request , 'register.html')

def login(request):
    if request.method == 'POST':
        username= request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            messages.info(request,'Loged in')
            return redirect('login')
        else:
            messages.info(request,'username or password not correct')
            return redirect('login')
    else :
        return render(request , 'login.html')