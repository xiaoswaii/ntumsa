from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from itertools import chain
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return HttpResponse("hello");

@login_required
def contactlist(request):
	return render(request,'contactlist.html',locals())

def index(request):
	if request.method == "POST":
		username=request.POST["username"]
		password=request.POST["pass"]
		user=auth.authenticate(username=username,password=password)
		if user is not None and user.is_active:
			auth.login(request,user)
			return redirect('contactlist')
		else:
			return render(request, 'index.html', locals())
	return render(request, 'index.html', locals())


