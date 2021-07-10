from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth
from .models import *
# Create your views here.


def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        name=request.POST['name']
        if User.objects.filter(username=username).exists():
            return render(request,'Signup.html',{'error':"이미 존재하는 사용자입니다."})
        if password==request.POST['password_check']:
            user=User.objects.create_user(
                username, password=password
            )
            #auth.login(request,user)
            customer = Account(user=user, name = name, leader=0)
            customer.save()
            return render(request,'Main.html')
        else :
            return render(request,'Signup.html',{'error':"비밀번호 확인이 일치하지 않습니다"})
    else:
        return render(request,'Signup.html')

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            return render(request,'Login.html',{'error':"사용자 이름 혹은 패스워드가 일치하지 않습니다"})
    else:
        return render(request,'Login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def myClub(request):
    return render(request, "myClub.html")

def myClubEdit(request):
    return render(request,"myClubEdit.html")

