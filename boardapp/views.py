from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import BoardModel
from django.views.generic.edit import CreateView,UpdateView
from django.urls import reverse_lazy, reverse
from django.views.decorators.http import require_POST

def signupfunc(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST["password"]
        try:
            user = User.objects.create_user(username,'', password)
        except IntegrityError:
            #ここでのエラーはsignup.htmlの中につながっている
           return render(request,'signup.html',{'error': 'このユーザーは登録されています。'})

    return redirect("login")

def loginfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return render(request,'login.html',{'context' : "not logged in"})

    return render(request,'login.html',{'context' : "get method"})

#@login_required ログインしているか確認
def listfunc(request):
    object_list = BoardModel.objects.order_by('-date').all()
    return render(request,'list.html',{"object_list" : object_list})
    
def logoutfunc(request):
    logout(request)
    return redirect("login")

#画面の詳細
def detailfunc(request, pk): 
    #対象のオブジェクトがない場合は404エラー
    object = get_object_or_404(BoardModel, pk=pk)
    return render(request,'detail.html',{ "object" : object ,"authuser" : request.user.get_username()})

#いいねの追加
def goodfunc(request, pk): 
    object = BoardModel.objects.get(pk=pk)
    object.good += 1
    object.save()
    return redirect('list')

#既読の追加
def readfunc(request, pk): 
    object = BoardModel.objects.get(pk=pk)
    username = request.user.get_username()
    #既読済みの場合
    if username in object.readtext:
        return redirect('list')
    #既読じゃない場合
    else:   
        object.read += 1
        object.readtext = object.readtext + ' ' +username
        object.save()
        return redirect('list')

#@require_POST #ボタンが押されたときのみ削除
def deletefunc(request, pk):
    object = get_object_or_404(BoardModel, pk=pk)
    object.delete()
    return redirect("list")


#投稿内容の編集機能
class BoardUpdate(UpdateView):
    template_name = "edit.html"
    model = BoardModel
    fields = ("title","content","author","snsimage")
    success_url = reverse_lazy("list")

#投稿内容の新規作成
class BoardCreate(CreateView):
    template_name = "create.html"
    model = BoardModel
    fields = ("title","content","author","snsimage")
    #投稿が成功した際のURL
    success_url = reverse_lazy("list")

    #form.pyを使う場合
# def create(request):
#     if request.method == "POST":
#         form = BoardForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect("list")
#     else:
#         form = BoardForm()
#     return render(request,'create.html',{"form" : form})
