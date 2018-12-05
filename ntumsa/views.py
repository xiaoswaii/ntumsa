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

def index(request):
	return render(request, 'index.html', locals())
