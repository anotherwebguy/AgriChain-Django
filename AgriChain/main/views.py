from django.shortcuts import render
from django.http import HttpResponseBadRequest
import pyrebase
from django.contrib import auth as authe
from datetime import datetime
from django.shortcuts import redirect
from web3 import Web3
import json
from django.http import JsonResponse
import pyqrcode
from pyqrcode import QRCode


# Create your views here.
def index(request):
    return render(request,'main/home.html')
    
def signup(request):
    return render(request,'main/signup.html')

def login(request):
    return render(request,'main/signin.html')    

def home(request):
    return render(request,'main/index.html')

def about(request):
    return render(request,'main/about.html')   

def contact(request):
    return render(request,'main/contact.html')

def blog(request):
    return render(request,'main/blog.html')

def services(request):
    return render(request,'main/services.html')

def gallery(request):
    return render(request,'main/gallery.html')

def typo(request):
    return render(request,'main/typo.html')
