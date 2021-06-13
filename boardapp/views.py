from django.shortcuts import render
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login

def signupfunc(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST["password"]
        try:
            user = User.objects.create_user(username,'', password)
        except IntegrityError:
            #ここでのエラーはsignup.htmlの中につながっている
           return render(request,'signup.html',{'error': 'このユーザーは登録されています。'})

    return render(request,'signup.html',{'some' : 100})

def loginfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request,'login.html',{'context' : "logged in"})
        else:
            return render(request,' login.html',{'context' : "not logged in"})

    return render(request,'login.html',{'context' : "get method"})

def listfunc(request):
    return render(request,'list.html',{})

        
